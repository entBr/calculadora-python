"""Pruebas de las operaciones, sin depender del menú."""

import unittest

from calculadora import dividir, multiplicar, restar, sumar


class OperacionesTests(unittest.TestCase):
    def test_sumar(self):
        for a, b, esperado in [(2, 3, 5), (-2, -3, -5), (-2, 3, 1), (0, 0, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(sumar(a, b), esperado)

    def test_restar(self):
        for a, b, esperado in [(7, 2, 5), (2, 7, -5), (-2, -3, 1), (0, 0, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(restar(a, b), esperado)

    def test_multiplicar(self):
        for a, b, esperado in [(2, 3, 6), (-2, 3, -6), (-2, -3, 6), (8, 0, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(multiplicar(a, b), esperado)

    def test_dividir(self):
        for a, b, esperado in [(8, 2, 4), (7, 2, 3.5), (-6, 2, -3), (-6, -2, 3), (0, 5, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(dividir(a, b), esperado)

    def test_decimales(self):
        self.assertAlmostEqual(sumar(0.1, 0.2), 0.3)
        self.assertAlmostEqual(restar(0.3, 0.1), 0.2)
        self.assertAlmostEqual(multiplicar(0.1, 0.2), 0.02)
        self.assertAlmostEqual(dividir(1, 3), 0.3333333333333333)

    def test_dividir_entre_cero(self):
        for numerador in [1, 0, -1]:
            with self.subTest(numerador=numerador):
                with self.assertRaisesRegex(ValueError, "No se puede dividir entre cero"):
                    dividir(numerador, 0)


if __name__ == "__main__":
    unittest.main()
