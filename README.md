# Pasis Medios de Pago

## Comop ejecutar

```bash

export PORT=8000
export HOST="0.0.0.0"
export ENV="development"
export WORKERS=4

uvicorn main:app --host ${HOST} --port ${PORT} --reload --workers ${WORKERS}
```
