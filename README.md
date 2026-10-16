# Calculadora en Python

Aplicación de consola con suma, resta, multiplicación, división e IMC. Usa Python 3.10 o superior. Proyecto reutilizado con autorización para la actividad de integración continua.

## Ejecutar

Desde la carpeta del repositorio:

```sh
python -m pip install -r requirements.txt
python app.py
```

Selecciona una operación e introduce dos números. Se admiten números negativos y decimales con punto o coma. La opción `0` cierra la aplicación.

La opción `5` calcula el IMC: solicita peso en kilogramos y altura en metros.
`imc(peso, altura)` devuelve `peso / altura**2` sin redondear. Solo acepta
enteros y decimales positivos y finitos; los tipos incorrectos (incluidos
booleanos) producen `TypeError`, y los valores inválidos o fuera del rango
numérico producen `ValueError`.

## Estructura

- `calculadora.py`: funciones de cálculo independientes de la interfaz.
- `app.py`: menú, entrada de datos y presentación de resultados.
- `tests/`: pruebas de operaciones, validación de entradas y menú.

## Practicar la creación de tests

Las pruebas de IMC usan `pytest`, incluido en `requirements.txt`. Pytest también
ejecuta las pruebas existentes de `unittest`. `tests/test_imc.py` cubre un caso
correcto, un peso positivo cercano a cero, entradas inválidas y límites numéricos.

Casos sugeridos:

- Operaciones con números positivos, negativos y cero.
- Resultados con decimales; comparar con tolerancia.
- División entre cero: debe lanzar `ValueError`.
- Entrada inválida y selección de opciones en la interfaz.
- Importar `app` no debe iniciar el menú.

Para ejecutar todos los tests:

```sh
python -m pytest -v
```

## Pruebas automáticas en GitHub

El workflow `.github/workflows/ci.yml` ejecuta las pruebas con Python 3.10
en cada push a `main`. Instala las dependencias y ejecuta `python -m pytest -v`.
También puedes iniciarlo manualmente desde **Actions**.

## Publicar la calculadora en GitHub Pages

El workflow `.github/workflows/pages.yml` publica `index.html` en GitHub Pages
en cada push a `main`; también puedes ejecutarlo manualmente desde **Actions**.
Para habilitar la publicación inicial, abre **Settings > Pages** del repositorio
y selecciona **GitHub Actions** como fuente de despliegue. La URL del sitio
aparecerá en la ejecución del workflow y en **Settings > Pages**.

## Demostración verde rojo verde

1. Ejecutar las pruebas, guardar la implementación en un commit y subirlo a
   `main`. Conservar la captura y el enlace de la ejecución verde en Actions.
2. En `tests/test_imc.py`, cambiar el valor esperado de `test_imc_correcto`
   de `22.8571428571` a `30.0`. Guardar otro commit y subirlo a `main`.
   Conservar la evidencia del fallo en el paso de pytest.
3. Restaurar `22.8571428571`, ejecutar las pruebas, guardar un tercer commit
   y subirlo a `main`. Conservar la evidencia de recuperación en verde.

Las tres capturas deben mostrar ejecuciones reales y sus commits asociados.
Las pruebas locales no sustituyen las evidencias de GitHub Actions.

## Git

Este directorio es un repositorio Git local. Para revisar los cambios:

```sh
git status
git diff
```
