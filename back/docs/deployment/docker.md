# Docker

Levantar proyecto:

```bash
docker compose up --build
```

---

# Detener

```bash
docker compose down
```

---

# Reiniciar limpio

```bash
docker compose down -v
docker compose up --build
```

---

# Ver logs

```bash
docker logs -f xkala_backend
```