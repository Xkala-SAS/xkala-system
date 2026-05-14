# Sistema de Permisos

Xkala implementa RBAC (Role Based Access Control).

---

# Roles

- Super Admin
- Gestion Humana
- Supervisor
- Empleado
- Auditor
- Gerencia
- Practicante

---

# Permisos

Ejemplos:

- create_user
- update_user
- view_users
- upload_documents
- delete_documents

---

# Relación

```text
Role
→ tiene permisos
→ permisos protegen endpoints
```

---

# Protección de endpoints

Ejemplo:

```python
Depends(require_permission("create_user"))
```

---

# Roles

Ejemplo:

```python
Depends(require_role("Super Admin"))
```

---

# JWT

La autenticación usa Bearer Token JWT.

---

# Middleware de auditoría

Todas las requests son auditadas:

- endpoint
- método
- IP
- user agent
- status code
- usuario