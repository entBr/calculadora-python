"""Calculadora interactiva de consola."""

import math

from calculadora import dividir, imc, multiplicar, restar, sumar


OPERACIONES = {
    "1": ("Sumar", sumar),
    "2": ("Restar", restar),
    "3": ("Multiplicar", multiplicar),
    "4": ("Dividir", dividir),
    "5": ("Calcular IMC", imc),
}


def leer_numero(mensaje: str) -> float:
    while True:
        try:
            numero = float(input(mensaje).strip().replace(",", "."))
            if not math.isfinite(numero):
                raise ValueError
            return numero
        except ValueError:
            print("Introduce un número válido y finito.")


def main() -> None:
    print("Calculadora en Python")
    while True:
        print("\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Calcular IMC\n0. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "0":
            print("¡Hasta luego!")
            return
        if opcion not in OPERACIONES:
            print("Opción inválida. Elige entre 0 y 5.")
            continue
        a = leer_numero("Peso en kilogramos: " if opcion == "5" else "Primer número: ")
        b = leer_numero("Altura en metros: " if opcion == "5" else "Segundo número: ")
        try:
            resultado = OPERACIONES[opcion][1](a, b)
            print(f"Resultado: {resultado:g}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\n¡Hasta luego!")
