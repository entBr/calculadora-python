"""Sondeo puntual de salud; no acredita un SLA mensual."""
import datetime
import json
import math
import sys
import time
from urllib.request import urlopen

url = sys.argv[1].rstrip("/") + "/health"
cantidad = int(sys.argv[2]) if len(sys.argv) > 2 else 1
muestras = []
for _ in range(cantidad):
    inicio = time.perf_counter()
    try:
        with urlopen(url, timeout=20) as r:
            codigo = r.status
            correcto = codigo == 200 and json.loads(r.read()) == {"status": "ok"}
    except Exception as error:
        codigo, correcto = str(type(error).__name__), False
    muestras.append({"estado": codigo, "ok": correcto,
                     "ms": round((time.perf_counter()-inicio)*1000, 2)})
exitos = [m["ms"] for m in muestras if m["ok"]]
resumen = {"fecha_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "url": url, "muestras": muestras,
           "exito_muestra_pct": len(exitos)/cantidad*100,
           "p95_ms": sorted(exitos)[math.ceil(.95*len(exitos))-1] if exitos else None}
print(json.dumps(resumen, ensure_ascii=False, indent=2))
sys.exit(0 if len(exitos) == cantidad else 1)
