"""Pruebas de entrada y sesiones completas de la calculadora."""

import io
from pathlib import Path
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from app import leer_numero, main


class EntradaTests(unittest.TestCase):
    def test_acepta_enteros_decimales_y_espacios(self):
        for entrada, esperado in [("42", 42), ("-3.5", -3.5), (" 2,75 ", 2.75), ("0", 0)]:
            with self.subTest(entrada=entrada), patch("builtins.input", return_value=entrada):
                self.assertEqual(leer_numero("Número: "), esperado)

    def test_reintenta_entradas_invalidas_y_no_finitas(self):
        for entrada in ["texto", "", "NaN", "inf", "-inf", "1e999"]:
            with self.subTest(entrada=entrada):
                salida = io.StringIO()
                with patch("builtins.input", side_effect=[entrada, "5"]), redirect_stdout(salida):
                    self.assertEqual(leer_numero("Número: "), 5)
                self.assertIn("Introduce un número válido y finito.", salida.getvalue())


class MenuTests(unittest.TestCase):
    def ejecutar_menu(self, entradas):
        salida = io.StringIO()
        with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
            main()
        return salida.getvalue()

    def test_operaciones_desde_el_menu(self):
        for opcion, esperado in [("1", "9"), ("2", "3"), ("3", "18"), ("4", "2")]:
            with self.subTest(opcion=opcion):
                salida = self.ejecutar_menu([opcion, "6", "3", "0"])
                self.assertIn(f"Resultado: {esperado}\n", salida)
                self.assertIn("¡Hasta luego!", salida)

    def test_opcion_invalida_permite_continuar(self):
        salida = self.ejecutar_menu(["9", "1", "2", "3", "0"])
        self.assertIn("Opción inválida", salida)
        self.assertIn("Resultado: 5\n", salida)

    def test_division_entre_cero_permite_continuar(self):
        salida = self.ejecutar_menu(["4", "1", "0", "1", "2", "3", "0"])
        self.assertIn("Error: No se puede dividir entre cero.", salida)
        self.assertIn("Resultado: 5\n", salida)

    def test_salir_sin_pedir_numeros(self):
        salida = self.ejecutar_menu(["0"])
        self.assertIn("¡Hasta luego!", salida)
        self.assertNotIn("Resultado:", salida)

    def test_importar_app_no_inicia_el_menu(self):
        resultado = subprocess.run(
            [sys.executable, "-c", "import app"],
            cwd=Path(__file__).resolve().parents[1],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertEqual(resultado.stdout, "")


if __name__ == "__main__":
    unittest.main()
