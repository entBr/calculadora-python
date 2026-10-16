"""Casos correctos, límites y errores del cálculo de IMC."""

import pytest

from calculadora import imc


def test_imc_correcto():
    assert imc(70, 1.75) == pytest.approx(2.8571428571)


def test_imc_limite_positivo():
    assert imc(0.001, 1.0) == pytest.approx(0.001)


@pytest.mark.parametrize("peso, altura", [
    (0, 1.75), (-70, 1.75), (70, 0), (70, -1.75),
    (float("nan"), 1.75), (70, float("nan")),
    (float("inf"), 1.75), (70, float("inf")),
    (float("-inf"), 1.75), (70, float("-inf")),
])
def test_imc_valores_invalidos(peso, altura):
    with pytest.raises(ValueError, match="positivo y finito"):
        imc(peso, altura)


@pytest.mark.parametrize("peso, altura", [
    ("70", 1.75), (70, "1.75"), (True, 1.75), (70, False),
    (None, 1.75), (70, None),
])
def test_imc_tipos_invalidos(peso, altura):
    with pytest.raises(TypeError, match="debe ser un número"):
        imc(peso, altura)


@pytest.mark.parametrize("peso, altura", [
    (10 ** 400, 1.75), (70, 1e-300), (70, 1e300),
    (1e308, 1e-10), (1e-300, 1e100),
])
def test_imc_fuera_de_rango(peso, altura):
    with pytest.raises(ValueError):
        imc(peso, altura)
