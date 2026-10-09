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
- `tests/`: carpeta reservada para los tests que crearás después.

## Practicar la creación de tests

El repositorio se entrega sin tests. Puedes empezar creando `tests/test_calculadora.py` con `unittest` (incluido en Python) o con `pytest`.

Casos sugeridos:

- Operaciones con números positivos, negativos y cero.
- Resultados con decimales; comparar con tolerancia.
- División entre cero: debe lanzar `ValueError`.
- Entrada inválida y selección de opciones en la interfaz.
- Importar `app` no debe iniciar el menú.

Para ejecutar futuros tests con `unittest`:

```sh
python -m unittest discover -s tests -v
```

## Git

Este directorio es un repositorio Git local. Para revisar los cambios:

```sh
git status
git diff
```
