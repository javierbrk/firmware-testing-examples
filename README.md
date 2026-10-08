# Ejemplos de testing de firmware

Ejemplos de la sección *17 · Ejemplos* (Ingeniería de Software · Firmware):

| Ejemplo | Archivo |
|---|---|
| Prueba unitaria (pytest) | `tests/unit/test_crc.py` |
| Mock de dependencia (monkeypatch) | `tests/unit/test_radio_client.py` |
| Sistema con Labgrid | `tests/hil/test_boot_shell.py` |
| Aceptación | `tests/hil/test_acceptance_net.py` |
| Gate de CI | `.github/workflows/ci.yml` |

## Uso

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Sin hardware (unit + sil)
pytest -m "not labgrid"

# Con hardware (ajustar labgrid/env.yaml)
BUILD_VERSION=1.2.3 pytest -m labgrid --lg-env labgrid/env.yaml
```

## Notas
- `src/` contiene el código bajo prueba (`crc8`, `RadioClient`) creado para que los ejemplos corran.
- `labgrid/env.yaml` y la strategy son plantillas: adaptar a tu DUT.
- `tests/sil/` es un placeholder para que el job `sil` no falle por falta de tests.
