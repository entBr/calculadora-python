"""Operaciones de la calculadora, independientes de la interfaz."""

import math


def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def imc(peso: float, altura: float) -> float:
    """Calcula peso / altura**2 sin redondear, en kg/m².

    Args:
        peso: Número positivo y finito en kilogramos.
        altura: Número positivo y finito en metros.
    Raises:
        TypeError: Si una entrada no es int o float, o es booleana.
        ValueError: Si una entrada no es positiva y finita o el
            resultado está fuera del rango numérico representable.
    Returns:
        Índice de masa corporal sin redondear.
    """
    for nombre, valor in (("peso", peso), ("altura", altura)):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError(f"{nombre} debe ser un número.")
        try:
            valido = math.isfinite(valor) and valor > 0
        except OverflowError:
            valido = False
        if not valido:
            raise ValueError(f"{nombre} debe ser positivo y finito.")
    try:
        resultado = peso / (altura ** 2)
    except (OverflowError, ZeroDivisionError) as error:
        raise ValueError("Valores fuera del rango de cálculo.") from error
    if not math.isfinite(resultado) or resultado <= 0:
        raise ValueError("Resultado fuera del rango de cálculo.")
    return resultado
