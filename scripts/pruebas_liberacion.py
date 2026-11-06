"""Pruebas HTTP contra un servicio ya desplegado."""
import json
import sys
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

BASE = sys.argv.pop(1).rstrip("/") if len(sys.argv) > 1 else "http://127.0.0.1:8080"

class PruebasHTTP(unittest.TestCase):
    def solicitar(self, ruta, metodo="GET"):
        try:
            with urlopen(Request(BASE + ruta, method=metodo), timeout=20) as r:
                return r.status, r.read()
        except HTTPError as error:
            return error.code, error.read()

    def test_interfaz_publicada(self):
        estado, cuerpo = self.solicitar("/")
        self.assertEqual(estado, 200)
        self.assertIn(b'calculator-form', cuerpo)
        self.assertIn(b'result-value', cuerpo)

    def test_salud(self):
        estado, cuerpo = self.solicitar("/health")
        self.assertEqual(estado, 200)
        self.assertEqual(json.loads(cuerpo), {"status": "ok"})

    def test_ruta_inexistente(self):
        estado, _ = self.solicitar("/ruta-inexistente-u2")
        self.assertEqual(estado, 404)

    def test_metodo_no_permitido(self):
        estado, _ = self.solicitar("/health", "POST")
        self.assertEqual(estado, 405)

if __name__ == "__main__":
    unittest.main(verbosity=2)
