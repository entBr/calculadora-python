# Calculadora en Python

Aplicación de consola con suma, resta, multiplicación y división. Usa Python 3.10 o superior y no requiere paquetes externos.

## Ejecutar

Desde la carpeta del repositorio:

```sh
python app.py
```

Selecciona una operación e introduce dos números. Se admiten números negativos y decimales con punto o coma. La opción `0` cierra la aplicación.

## Estructura

- `calculadora.py`: funciones de cálculo independientes de la interfaz.
- `app.py`: menú, entrada de datos y presentación de resultados.
- `tests/`: pruebas de operaciones, validación de entradas y menú.

## Practicar la creación de tests

Las pruebas usan `unittest`, incluido en Python, sin paquetes externos. Puedes ampliarlas para practicar nuevos casos o adaptarlas a `pytest`.

Casos sugeridos:

- Operaciones con números positivos, negativos y cero.
- Resultados con decimales; comparar con tolerancia.
- División entre cero: debe lanzar `ValueError`.
- Entrada inválida y selección de opciones en la interfaz.
- Importar `app` no debe iniciar el menú.

Para ejecutar todos los tests:

```sh
python -m unittest discover -s tests -v
```

## Pruebas automáticas en GitHub

El workflow `.github/workflows/tests.yml` ejecuta las pruebas con Python 3.10,
3.11, 3.12, 3.13 y 3.14 en cada push y pull request. También puedes iniciarlo
manualmente desde la pestaña **Actions** del repositorio.

## Git

Este directorio es un repositorio Git local. Para revisar los cambios:

```sh
git status
git diff
```
