# Users API

---

# Login

POST `/users/login`

## Request

```json
{
  "numero_documento": "1000000000",
  "password": "Admin123*"
}
```

---

# Crear usuario

POST `/users/`

Requiere permiso:

```text
create_user
```

---

# Obtener perfil

GET `/users/me`

---

# Upload foto perfil

POST `/users/upload/profile-photo`

---

# Upload firma

POST `/users/upload/signature`

---

# Upload documento

POST `/users/upload/document`

Query params:

```text
document_type=cedula
```

---

# Listar documentos

GET `/users/my-documents`

---

# Eliminar documento

DELETE `/users/document/{id}`