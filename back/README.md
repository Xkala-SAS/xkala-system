# Xkala System API

Backend ERP desarrollado con FastAPI siguiendo arquitectura hexagonal.

---

# Tecnologías

- FastAPI
- SQLAlchemy
- MySQL
- Docker
- Alembic
- JWT Authentication
- RBAC Permissions
- Swagger/OpenAPI

---

# Arquitectura

El proyecto implementa arquitectura hexagonal:

- interfaces
- application
- domain
- infrastructure
- core

---

# Características

- Autenticación JWT
- Roles y permisos
- Auditoría de requests
- Upload de archivos
- Soft delete
- Gestión documental
- Seeders automáticos
- Dockerized environment

---

# Levantar proyecto

## Docker

```bash
docker compose up --build
```

---

# Ejecutar migraciones

```bash
alembic upgrade head
```

---

# Ejecutar seeders

```bash
python -m app.infrastructure.database.seeds.run_seeds
```

---

# Swagger

Disponible en:

```text
http://localhost:8000/docs
```

---

# Variables de entorno

Usa:

- .env.dev
- .env.prod

---

# Estructura del proyecto

```text
app/
│
├── application
├── core
├── domain
├── infrastructure
└── interfaces
```

---

# Seguridad

El sistema implementa:

- JWT Authentication
- Role Based Access Control (RBAC)
- Middleware de auditoría
- Validación de permisos

---

# Estado actual

Módulos implementados:

- Usuarios
- Roles
- Permisos
- Uploads
- Auditoría
- Gestión documental