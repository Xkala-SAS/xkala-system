# Xkala System ERP

ERP backend desarrollado con FastAPI siguiendo arquitectura hexagonal.

---

# Arquitectura

```text
back/   → FastAPI ERP Backend
front/  → Angular ERP Frontend
docs/   → Documentación técnica
```

---

# Tecnologías

## Backend

- FastAPI
- SQLAlchemy
- MySQL
- Alembic
- JWT
- Docker

## Frontend (próximamente)

- Angular
- RxJS
- Bootstrap / PrimeNG

---

# Características

- JWT Authentication
- RBAC Permissions
- Audit Logs
- File Uploads
- Soft Delete
- Swagger Documentation
- Dockerized Environment

---

# Levantar proyecto

```bash
docker compose up --build
```

---

# Swagger

```text
http://localhost:8000/docs
```

---

# Credenciales Demo

## Super Admin

Documento:

```text
1000000000
```

Password:

```text
Admin123*
```

---

# Estructura

```text
xkala-system/
│
├── back/
├── front/
├── docs/
├── screenshots/
└── docker-compose.yml
```
