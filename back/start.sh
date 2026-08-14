#!/bin/sh

echo "⏳ Esperando MySQL..."

until python -c "
import socket
s=socket.socket()
s.settimeout(2)
s.connect(('mysql',3306))
s.close()
"
do
    echo "⌛ MySQL aún no está listo..."
    sleep 2
done

echo "✅ Puerto MySQL disponible"

sleep 5

echo "🚀 Ejecutando migraciones..."
alembic upgrade head

echo "🌱 Ejecutando seeds..."
python -m app.infrastructure.database.seeds.run_seeds

echo "🔥 Iniciando FastAPI..."
exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port 8000 \
    --proxy-headers \
    --forwarded-allow-ips="*"