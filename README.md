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

## CI y despliegue en GitHub

El workflow `.github/workflows/ci.yml` ejecuta las pruebas con Python 3.10 y,
si pasan, publica `index.html` en GitHub Pages. Se inicia en cada push a `main`
y también se puede ejecutar manualmente desde **Actions**. Para habilitar la
publicación inicial, selecciona **GitHub Actions** como fuente en
**Settings > Pages**. La URL aparece en la ejecución del workflow y en
**Settings > Pages**.

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

## Despliegue en Railway

La interfaz index.html realiza los cálculos en JavaScript. web.py la sirve con Flask; la calculadora de consola permanece en app.py. El contenedor ejecuta Gunicorn y escucha en 0.0.0.0 y el puerto PORT asignado por Railway.

1. En Railway crea un proyecto desde entBr/calculadora-python y selecciona main.
2. Usa el Dockerfile de la raíz y railway.toml. No agregues un comando de inicio alternativo.
3. En Source activa autodeploy y Wait for CI. El workflow CI para Railway debe finalizar correctamente antes del despliegue.
4. Genera un dominio público en Networking. Comprueba / y /health.
5. Para demostrar CD cambia un texto visible en index.html, haz commit y push a main y conserva el SHA, la ejecución verde y el nuevo deployment automático con el mismo SHA.

El workflow comprueba pytest y construye y prueba el contenedor. El CD lo ejecuta la integración nativa de Railway. No requiere guardar un token de Railway en GitHub.

Pruebas locales: python -m pip install -r requirements.txt -r requirements-web.txt; python -m pytest -v
