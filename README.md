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

## Integración continua

El workflow CI para Railway ejecuta Python 3.12, pytest, la construcción Docker
y cuatro pruebas HTTP del contenedor. Se dispara con push y pull_request a main,
y admite ejecución manual. La publicación del servicio se configura en Railway.

## Git

Este directorio es un repositorio Git local. Para revisar los cambios:

```sh
git status
git diff
```

## Despliegue en Railway

Flask sirve index.html en / y devuelve JSON en /health. Gunicorn escucha PORT.
Configurar Source con este repositorio y main, autodeploy y Wait for CI.
El builder detecta Dockerfile. En el panel establecer Healthcheck Path=/health,
tiempo de espera de 120 segundos y 3 reinicios ante fallo. Revisar los valores
efectivos del servicio; railway.toml se conserva como configuración original,
pero no se supone aplicado en servicios nuevos si Railway no permite Config as Code.
Generar un dominio público y comprobar / y /health.

Pruebas de liberación contra un servicio ya desplegado:
python scripts/pruebas_liberacion.py https://DOMINIO_REAL

Preparación local en Linux o Git Bash:
bash scripts/preparar_entorno.sh

El script HTTP verifica interfaz, JSON de salud, ruta inexistente y POST rechazado.
No sustituye las comprobaciones de JavaScript en un navegador.
