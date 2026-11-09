import unittest
from web import app

class PruebasAzure(unittest.TestCase):
    def test_interfaz(self):
        respuesta = app.test_client().get('/')
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn(b'calculator-form', respuesta.data)
    def test_salud(self):
        respuesta = app.test_client().get('/health')
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.get_json(), {'status': 'ok'})

if __name__ == '__main__':
    unittest.main(verbosity=2)
