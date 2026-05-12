#!/bin/sh

echo "⏳ Esperando MySQL..."

sleep 10

echo "🚀 Ejecutando migraciones..."

alembic upgrade head

echo "🌱 Ejecutando seeds..."

python -m app.infrastructure.database.seeds.run_seeds

echo "🔥 Iniciando FastAPI..."

uvicorn app.main:app --host 0.0.0.0 --port 8000