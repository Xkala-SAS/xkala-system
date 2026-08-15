# XKALA System — Development Setup

Guía oficial para desarrolladores que se integren al proyecto XKALA System.

---

## 1. Descripción

XKALA System es un ERP empresarial compuesto por:

- Backend REST API
- Frontend web
- Base de datos MySQL
- Nginx
- Docker

El Backend utiliza arquitectura hexagonal para separar la lógica de negocio, la aplicación, las interfaces y la infraestructura.

---

## 2. Stack tecnológico

### Backend

- Python 3.12
- FastAPI
- SQLAlchemy
- MySQL 8.4
- Alembic
- JWT
- bcrypt
- Pydantic Settings

### Frontend

- Angular 20
- TypeScript
- RxJS
- PrimeNG
- Bootstrap
- SCSS

### Infraestructura

- Docker
- Docker Compose
- Nginx
- MySQL

## 3. Estructura del proyecto

XKALA System está organizado como un sistema empresarial separado por responsabilidades.

La estructura principal del proyecto es:

~~~text
xkala-system/
│
├── back/                  # Backend — FastAPI
├── front/                 # Frontend — Angular
├── nginx/                 # Reverse Proxy
├── docs/                  # Documentación técnica
├── screenshots/           # Evidencias visuales
│
├── docker-compose.yml     # Entorno de producción
├── docker-compose.dev.yml # Entorno de desarrollo
└── README.md              # Documentación principal
~~~

### `back/` — Backend

Contiene toda la aplicación Backend del ERP.

~~~text
back/
│
├── alembic/               # Migraciones de base de datos
├── app/                   # Código fuente de la aplicación
├── tools/                 # Herramientas auxiliares
├── uploads/               # Archivos gestionados por la aplicación
│
├── Dockerfile             # Imagen Docker de producción
├── Dockerfile.dev         # Imagen Docker de desarrollo
├── requirements.txt       # Dependencias Python
└── start.sh               # Proceso de inicio del Backend
~~~

El código de negocio y aplicación debe permanecer dentro de:

~~~text
back/app/
~~~

Las migraciones de base de datos se gestionan mediante Alembic y se almacenan en:

~~~text
back/alembic/versions/
~~~

### `front/` — Frontend

Contiene la aplicación web desarrollada con Angular.

~~~text
front/
│
├── src/                   # Código fuente Angular
├── public/                # Recursos públicos
│
├── angular.json           # Configuración Angular
├── package.json           # Dependencias y scripts
├── package-lock.json      # Versiones bloqueadas
│
├── Dockerfile             # Imagen Docker de producción
└── Dockerfile.dev         # Imagen Docker de desarrollo
~~~

La lógica de presentación, componentes, servicios y funcionalidades del ERP debe permanecer dentro de:

~~~text
front/src/
~~~

### `nginx/` — Reverse Proxy

Contiene la configuración de Nginx utilizada para enrutar las peticiones del sistema.

~~~text
nginx/
│
├── conf.d/
│   └── xkala.conf
│
├── Dockerfile
└── nginx.conf
~~~

Nginx actúa como punto de entrada del sistema en el entorno de producción.

### `docs/` — Documentación

Toda la documentación técnica debe mantenerse dentro de:

~~~text
docs/
~~~

La estructura documental es:

~~~text
docs/
│
├── api/                    # Documentación de APIs
├── architecture/           # Arquitectura del sistema
├── database/               # Base de datos y migraciones
├── deployment/             # Despliegue e infraestructura
├── development/             # Guías para desarrolladores
├── security/               # Seguridad y permisos
└── testing/                # Estrategia y documentación de pruebas
~~~

La documentación debe actualizarse cuando un cambio modifica la arquitectura, infraestructura, API, seguridad o flujo de desarrollo.

### Docker

El proyecto mantiene configuraciones separadas para desarrollo y producción.

Desarrollo:

~~~text
docker-compose.dev.yml
~~~

Producción:

~~~text
docker-compose.yml
~~~

No se deben mezclar configuraciones de desarrollo y producción.

### Regla de organización

Antes de crear un nuevo archivo o módulo:

1. Identificar a qué dominio pertenece.
2. Identificar qué responsabilidad tiene.
3. Ubicarlo en la capa correspondiente.
4. Revisar la arquitectura existente.
5. Evitar duplicar responsabilidades existentes.

La estructura del proyecto es parte de la arquitectura y no debe modificarse arbitrariamente.

## 4. Requisitos previos

Antes de comenzar el desarrollo, el equipo debe contar con las siguientes herramientas instaladas y configuradas:

### Herramientas requeridas

- Git
- Docker
- Docker Compose
- Node.js 22
- npm
- Python 3.12

### Verificar instalaciones

~~~bash
git --version
docker --version
docker compose version
node --version
npm --version
python3 --version
~~~

### Repositorio

El proyecto utiliza Git para el control de versiones.

El repositorio remoto principal es:

~~~text
Xkala-SAS/xkala-system
~~~

Después de clonar el proyecto:

~~~bash
git clone <https://github.com/Xkala-SAS/xkala-system>
cd xkala-system
~~~

Antes de comenzar cualquier desarrollo, verificar el estado del repositorio:

~~~bash
git status
~~~

También se recomienda actualizar la rama de trabajo antes de comenzar:

~~~bash
git pull
~~~

### Docker

El proyecto está preparado para ejecutarse mediante Docker.

El entorno de desarrollo utiliza:

~~~text
docker-compose.dev.yml
~~~

El entorno de producción utiliza:

~~~text
docker-compose.yml
~~~

Los desarrolladores deben utilizar el entorno de desarrollo para trabajar localmente y evitar modificar directamente configuraciones destinadas a producción.

## 5. Configuración inicial del proyecto

Una vez clonado el repositorio, el proyecto debe configurarse utilizando el entorno de desarrollo.

### Levantar el entorno DEV

Desde la raíz del proyecto ejecutar:

~~~bash
docker compose -f docker-compose.dev.yml up --build
~~~

Para ejecutar los servicios en segundo plano:

~~~bash
docker compose -f docker-compose.dev.yml up --build -d
~~~

### Verificar los servicios

Comprobar que los contenedores estén ejecutándose:

~~~bash
docker compose -f docker-compose.dev.yml ps
~~~

El entorno de desarrollo está compuesto por:

~~~text
Frontend Angular
        │
        │ :4200
        ▼
Backend FastAPI
        │
        │ :8000
        ▼
MySQL
        │
        │ :3307
        ▼
Base de datos
~~~

### Accesos del entorno DEV

Frontend:

~~~text
http://localhost:4200
~~~

Backend:

~~~text
http://localhost:8000
~~~

Documentación Swagger:

~~~text
http://localhost:8000/docs
~~~

MySQL desde el equipo local:

~~~text
Host: localhost
Port: 3307
Database: xkala_system
~~~

Dentro de Docker, el Backend se conecta a MySQL mediante:

~~~text
Host: mysql
Port: 3306
~~~

### Variables de entorno

El Backend utiliza archivos de configuración independientes por entorno.

Desarrollo:

~~~text
back/.env.dev
~~~

Producción:

~~~text
back/.env.prod
~~~

Los archivos de entorno contienen configuración sensible, por lo que no deben incluirse en commits cuando contengan secretos reales.

### Verificación inicial

Una vez levantado el entorno, comprobar:

~~~bash
docker compose -f docker-compose.dev.yml ps
~~~

El Backend debe encontrarse ejecutándose en el puerto `8000` y el Frontend en el puerto `4200`.

Si alguno de los servicios no inicia correctamente, revisar primero los logs:

~~~bash
docker logs xkala_backend
docker logs xkala_frontend
docker logs xkala_mysql
~~~

## 6. Entornos de ejecución

XKALA System cuenta con configuraciones independientes para desarrollo y producción.

El objetivo es mantener separados los procesos de desarrollo local de la configuración utilizada para despliegue.

### Entorno de desarrollo

El entorno DEV utiliza:

~~~text
docker-compose.dev.yml
~~~

Características principales:

- Angular ejecutándose mediante `ng serve`.
- FastAPI ejecutándose mediante Uvicorn.
- MySQL ejecutándose dentro de Docker.
- Hot reload para Backend y Frontend.
- Código fuente montado mediante volúmenes Docker.
- Proxy de Angular para comunicación con el Backend.

Los servicios principales son:

~~~text
Frontend
localhost:4200
       │
       ▼
Angular Dev Server
       │
       │ /api
       ▼
FastAPI
localhost:8000
       │
       ▼
MySQL
localhost:3307
~~~

### Entorno de producción

El entorno de producción utiliza:

~~~text
docker-compose.yml
~~~

La arquitectura incorpora Nginx como punto de entrada:

~~~text
Cliente
   │
   ▼
Nginx
   │
   ├──► Frontend
   │
   └──► Backend
            │
            ▼
          MySQL
~~~

El acceso externo se realiza a través de Nginx.

En la configuración actual del proyecto, Nginx expone el puerto:

~~~text
localhost:8080
~~~

### Diferencias entre entornos

| Característica | DEV | PROD |
|---|---|---|
| Frontend | Angular Dev Server | Build de producción |
| Backend | FastAPI + Uvicorn | FastAPI + Uvicorn |
| Reverse Proxy | No | Nginx |
| Hot Reload | Sí | No |
| Docker Compose | `docker-compose.dev.yml` | `docker-compose.yml` |
| Frontend | `:4200` | A través de Nginx |
| Backend | `:8000` | A través de Nginx |
| MySQL | `:3307` | `:3307` |

### Regla de trabajo

El desarrollo de nuevas funcionalidades debe realizarse utilizando el entorno DEV.

El entorno PROD debe utilizarse únicamente para validar configuraciones y comportamientos destinados al despliegue.

No se deben utilizar credenciales, secretos o configuraciones de producción durante el desarrollo local.

## 7. Backend

El Backend de XKALA System está desarrollado con FastAPI y utiliza arquitectura hexagonal para separar las responsabilidades de la aplicación.

El código fuente principal se encuentra en:

~~~text
back/app/
~~~

### Estructura del Backend

~~~text
back/app/
│
├── application/       # Casos de uso y servicios de aplicación
├── core/              # Configuración y componentes transversales
├── domain/            # Dominio y reglas de negocio
├── infrastructure/   # Persistencia e infraestructura
├── interfaces/        # API y esquemas de entrada/salida
└── shared/            # Componentes compartidos
~~~

### `application/`

Contiene la lógica de aplicación que coordina los casos de uso del sistema.

Aquí se encuentran principalmente:

- Use Cases
- Application Services
- Mappers
- Dependencias relacionadas con casos de uso

Ejemplo:

~~~text
back/app/application/
│
├── services/
└── user/
    └── use_cases/
~~~

Los Use Cases representan acciones que el sistema puede ejecutar, por ejemplo:

~~~text
Crear usuario
Iniciar sesión
Cambiar contraseña
Guardar información personal
Gestionar contratos
~~~

### `domain/`

Contiene los elementos propios del dominio empresarial.

Incluye:

- Entidades
- Enums
- Interfaces de repositorios

El dominio no debe depender directamente de FastAPI, SQLAlchemy u otros detalles de infraestructura.

~~~text
back/app/domain/
│
└── user/
    ├── entities/
    ├── enums/
    └── repositories/
~~~

### `infrastructure/`

Contiene las implementaciones concretas relacionadas con infraestructura y persistencia.

Incluye:

- Modelos SQLAlchemy
- Repositorios
- Base de datos
- Migraciones y seeds
- Integraciones externas

~~~text
back/app/infrastructure/
│
├── database/
└── repositories/
~~~

### `interfaces/`

Contiene la entrada y salida de la aplicación.

Principalmente:

- Rutas HTTP
- Schemas
- Interfaces de API

~~~text
back/app/interfaces/
│
├── api/
└── schemas/
~~~

Las rutas reciben las peticiones HTTP y delegan la ejecución a los casos de uso correspondientes.

### `core/`

Contiene componentes transversales utilizados por diferentes partes de la aplicación.

Incluye elementos como:

- Seguridad
- JWT
- Excepciones
- Configuración
- Dependencias
- Respuestas
- Logging
- Middleware

~~~text
back/app/core/
~~~

### Regla de dependencia

La lógica de negocio no debe quedar acoplada directamente a detalles de infraestructura.

El flujo general esperado es:

~~~text
HTTP Request
     │
     ▼
Interface / Route
     │
     ▼
Use Case
     │
     ▼
Domain
     │
     ▼
Repository Interface
     │
     ▼
Repository Implementation
     │
     ▼
Database
~~~

Los nuevos desarrolladores deben revisar primero la arquitectura existente antes de introducir dependencias entre capas.

## 8. Frontend

El Frontend de XKALA System está desarrollado con Angular y utiliza una organización basada en dominios y componentes compartidos.

El código fuente principal se encuentra en:

~~~text
front/src/
~~~

### Estructura general

~~~text
front/src/
│
├── app/
│   ├── core/              # Funcionalidades centrales
│   ├── domains/           # Módulos y funcionalidades del negocio
│   └── shared/            # Componentes y recursos reutilizables
│
├── environments/          # Configuración por entorno
├── styles/                # Estilos globales y recursos de estilos
│
├── index.html
├── main.ts
└── styles.scss
~~~

### `app/core/`

Contiene funcionalidades centrales que son utilizadas por diferentes partes de la aplicación.

Aquí deben ubicarse elementos como:

- Guards
- Interceptors
- Servicios globales
- Configuraciones
- Manejo de autenticación
- Funcionalidades transversales

Estas funcionalidades no deben depender de un dominio específico.

### `app/domains/`

Contiene las funcionalidades propias de cada dominio del ERP.

Cada dominio debe mantener sus componentes, páginas, servicios y lógica relacionada agrupados dentro de su propio espacio.

Ejemplo:

~~~text
front/src/app/domains/
│
├── users/
├── hr/
├── onboarding/
├── dashboard/
└── ...
~~~

La lógica específica de un dominio debe permanecer dentro de dicho dominio siempre que sea posible.

### `app/shared/`

Contiene componentes, utilidades y elementos reutilizables entre diferentes dominios.

Ejemplos:

- Componentes UI
- Modales
- Tablas
- Formularios reutilizables
- Pipes
- Directivas
- Elementos visuales compartidos

~~~text
front/src/app/shared/
~~~

Un componente que sea específico de un único dominio no debe colocarse en `shared` únicamente para evitar crear una carpeta dentro del dominio.

### `environments/`

Contiene la configuración utilizada por Angular según el entorno.

~~~text
front/src/environments/
│
├── environment.ts
├── environment.development.ts
└── environment.production.ts
~~~

El entorno de desarrollo utiliza:

~~~text
environment.development.ts
~~~

El entorno de producción utiliza:

~~~text
environment.production.ts
~~~

La configuración de la API debe mantenerse centralizada mediante los archivos de entorno.

### Comunicación con el Backend

En desarrollo, el Frontend utiliza `/api` como ruta base para las peticiones HTTP.

La comunicación se realiza mediante el proxy configurado en:

~~~text
front/proxy.config.json
~~~

Flujo:

~~~text
Angular
   │
   │ /api
   ▼
Angular Dev Server
   │
   │ Proxy
   ▼
FastAPI
~~~

### Regla de organización

Antes de crear una nueva funcionalidad en el Frontend:

1. Identificar el dominio al que pertenece.
2. Revisar si ya existe un componente o servicio reutilizable.
3. Determinar si el elemento pertenece a `core`, `domains` o `shared`.
4. Evitar duplicar lógica.
5. Mantener los componentes enfocados en su responsabilidad.
6. Mantener la comunicación con la API encapsulada en servicios.

La estructura del Frontend debe mantener separadas las funcionalidades de negocio, las funcionalidades centrales y los elementos reutilizables.

## 9. Git y flujo de trabajo

XKALA System utiliza Git como sistema de control de versiones.

El objetivo es mantener un historial de cambios claro, facilitar el trabajo en equipo y evitar que los desarrolladores trabajen directamente sobre código compartido sin control.

### Rama principal

La rama `main` representa el código estable del proyecto.

No se debe desarrollar directamente sobre `main`.

~~~text
main
│
└── Código estable
~~~

Los cambios deben realizarse mediante ramas de trabajo y posteriormente integrarse mediante Pull Request.

### Flujo de trabajo

El flujo recomendado es:

~~~text
main
  │
  ├── feature/...
  │
  ├── fix/...
  │
  ├── refactor/...
  │
  └── docs/...
        │
        ▼
   Pull Request
        │
        ▼
      main
~~~

Cada desarrollador debe crear una rama específica para el trabajo que va a realizar.

### Crear una rama

Antes de comenzar una tarea, actualizar `main`:

~~~bash
git checkout main
git pull origin main
~~~

Crear posteriormente la rama de trabajo:

~~~bash
git checkout -b feature/nombre-de-la-funcionalidad
~~~

Ejemplo:

~~~bash
git checkout -b feature/user-onboarding
~~~

### Tipos de ramas

Las ramas deben utilizar prefijos que permitan identificar rápidamente el propósito del cambio.

| Prefijo | Uso |
|---|---|
| `feature/` | Nueva funcionalidad |
| `fix/` | Corrección de errores |
| `refactor/` | Refactorización sin cambio funcional |
| `docs/` | Cambios exclusivamente documentales |
| `test/` | Creación o modificación de pruebas |
| `chore/` | Mantenimiento técnico o configuración |

Ejemplos:

~~~text
feature/user-onboarding
feature/roles-management
fix/login-dev
fix/user-document-duplicate
refactor/user-repository
docs/update-development-guide
test/user-authentication
chore/update-dependencies
~~~

### Convención de commits

Los commits deben utilizar una convención consistente basada en:

~~~text
tipo(alcance): descripción
~~~

Ejemplos:

~~~text
feat(auth): add JWT login
fix(users): prevent duplicate documents
refactor(users): simplify user repository
docs(setup): update development environment
test(auth): add login tests
chore(docker): update development configuration
~~~

### Tipos de commit

| Tipo | Uso |
|---|---|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de un error |
| `refactor` | Cambio interno sin nueva funcionalidad |
| `docs` | Documentación |
| `test` | Pruebas |
| `chore` | Mantenimiento, configuración o dependencias |
| `perf` | Mejora de rendimiento |
| `style` | Cambios de formato sin modificar lógica |

### Reglas para los commits

Los commits deben ser:

- Pequeños y enfocados.
- Descriptivos.
- Relacionados con una única tarea.
- Escritos en inglés.
- Evitar mensajes genéricos como `update`, `changes`, `fix`, `test` o `final`.

Incorrecto:

~~~text
update
changes
fix
final
cosas
~~~

Correcto:

~~~text
feat(users): add employee registration
fix(auth): resolve development login issue
docs(api): document user endpoints
refactor(users): separate document repository
~~~

### Antes de hacer commit

Antes de crear un commit se recomienda revisar:

~~~bash
git status
~~~

Revisar los cambios:

~~~bash
git diff
~~~

Agregar únicamente los archivos relacionados con la tarea:

~~~bash
git add <archivo>
~~~

O agregar los cambios seleccionados:

~~~bash
git add -p
~~~

Crear el commit:

~~~bash
git commit -m "feat(users): add employee registration"
~~~

### Actualizar la rama antes de crear el Pull Request

Antes de solicitar la integración de una rama, actualizarla con los cambios recientes de `main`:

~~~bash
git checkout main
git pull origin main

git checkout feature/nombre-de-la-funcionalidad
git merge main
~~~

Resolver cualquier conflicto antes de crear el Pull Request.

### Pull Request

Las funcionalidades terminadas deben integrarse mediante Pull Request.

Un Pull Request debe incluir:

- Descripción del cambio.
- Motivo del cambio.
- Funcionalidades afectadas.
- Pruebas realizadas.
- Posibles consideraciones o riesgos.

No se debe realizar merge directamente sobre `main` sin revisión cuando el flujo del equipo requiera Pull Request.

### Regla principal

Cada cambio debe poder responder claramente a estas preguntas:

1. ¿Qué se modificó?
2. ¿Por qué se modificó?
3. ¿Qué archivos o módulos fueron afectados?
4. ¿Cómo se verificó el cambio?

El historial de Git debe permitir entender la evolución del proyecto sin necesidad de revisar manualmente todo el código.


## 10. Convenciones de desarrollo

Las siguientes convenciones deben seguirse al agregar o modificar código en XKALA System.

El objetivo es mantener una base de código consistente, fácil de mantener y alineada con la arquitectura definida.

### Principio de responsabilidad única

Cada archivo, clase, función o servicio debe tener una responsabilidad clara.

Evitar componentes o servicios que concentren demasiadas responsabilidades.

Incorrecto:

~~~text
UserService
├── crear usuario
├── autenticar usuario
├── subir documentos
├── enviar correos
├── generar reportes
└── modificar contratos
~~~

Preferible:

~~~text
UserService
AuthService
UserDocumentService
EmailService
ReportService
UserContractService
~~~

### No duplicar lógica

Antes de implementar una funcionalidad, revisar si ya existe una implementación que pueda reutilizarse.

Evitar:

- Duplicar validaciones.
- Duplicar consultas.
- Crear servicios con responsabilidades similares.
- Crear componentes visuales que ya existen.
- Repetir lógica de autenticación o autorización.

Cuando una lógica sea reutilizada por diferentes partes del sistema, evaluar si debe convertirse en un componente, servicio, utilidad o abstracción compartida.

### Backend

En el Backend se debe respetar la separación de responsabilidades definida por la arquitectura hexagonal.

Una nueva funcionalidad debe seguir, cuando corresponda, un flujo similar a:

~~~text
Route
  │
  ▼
Schema
  │
  ▼
Use Case
  │
  ▼
Domain
  │
  ▼
Repository Interface
  │
  ▼
Repository Implementation
  │
  ▼
Database
~~~

Las rutas no deben contener lógica de negocio compleja.

Ejemplo de responsabilidad de una Route:

~~~text
Recibir request
      ↓
Validar entrada
      ↓
Ejecutar Use Case
      ↓
Retornar respuesta
~~~

La lógica correspondiente a la operación debe permanecer en el Use Case o Service correspondiente.

### Frontend

En el Frontend se debe mantener una separación clara entre:

- Presentación.
- Lógica de aplicación.
- Acceso a datos.
- Componentes reutilizables.

Los componentes deben evitar concentrar lógica innecesaria.

La comunicación con el Backend debe realizarse mediante servicios.

Evitar realizar directamente múltiples llamadas HTTP desde los templates o mezclar lógica de acceso a datos con lógica visual.

### Nombres de archivos y clases

Los nombres deben ser descriptivos y representar claramente su responsabilidad.

Ejemplos Backend:

~~~text
create_user.py
login_user.py
user_repository.py
user_repository_impl.py
user_profile_mapper.py
~~~

Ejemplos Frontend:

~~~text
user.service.ts
auth.service.ts
user-profile.ts
user-profile.html
user-profile.scss
~~~

Evitar nombres genéricos como:

~~~text
helper.py
utils.py
service.py
data.py
manager.py
test2.py
~~~

cuando el nombre no permita conocer claramente su propósito.

### Variables y funciones

Las variables y funciones deben tener nombres descriptivos.

Evitar:

~~~python
u = repository.get(id)
x = service.execute(data)
d = request.data
~~~

Preferir:

~~~python
user = repository.get(user_id)
result = service.execute(user_data)
request_data = request.data
~~~

La claridad del código tiene prioridad sobre utilizar nombres excesivamente cortos.

### Comentarios

Los comentarios deben explicar el motivo de una decisión cuando esta no sea evidente.

Evitar comentarios que simplemente repitan lo que hace el código.

Incorrecto:

~~~python
# Obtener usuario
user = repository.get(user_id)
~~~

Preferible:

~~~python
# Se utiliza el repositorio para mantener el caso de uso
# desacoplado de SQLAlchemy.
user = repository.get(user_id)
~~~

Los comentarios no deben utilizarse para justificar código innecesariamente complejo. Si el código puede simplificarse, debe priorizarse la simplificación.

### Manejo de errores

Los errores deben gestionarse mediante los mecanismos establecidos por el Backend.

No se deben devolver respuestas HTTP manualmente desde diferentes partes de la aplicación sin seguir el sistema de excepciones definido.

Evitar:

~~~python
return {
    "error": "Something went wrong"
}
~~~

cuando exista una excepción específica para representar el error.

Los errores deben permitir distinguir entre situaciones como:

~~~text
Credenciales inválidas
Usuario inexistente
Usuario inactivo
Recurso no encontrado
Permiso insuficiente
Error de validación
Error interno
~~~

### Configuración

Las configuraciones dependientes del entorno no deben estar escritas directamente dentro del código fuente.

Utilizar los mecanismos de configuración existentes:

~~~text
.env.dev
.env.prod
environment.development.ts
environment.production.ts
~~~

No colocar secretos reales, contraseñas de producción, tokens o claves privadas directamente en el código.

### Dependencias

Antes de agregar una nueva dependencia:

1. Verificar si el proyecto ya dispone de una solución equivalente.
2. Revisar si la dependencia es realmente necesaria.
3. Evaluar su impacto en el proyecto.
4. Mantener actualizados los archivos de dependencias correspondientes.
5. Documentar cambios relevantes.

Backend:

~~~text
back/requirements.txt
~~~

Frontend:

~~~text
front/package.json
front/package-lock.json
~~~

### Cambios pequeños y controlados

Una tarea debe realizar cambios relacionados únicamente con su objetivo.

Evitar mezclar en el mismo commit:

~~~text
Nueva funcionalidad
+
Refactor completo
+
Cambio de estilos
+
Actualización de dependencias
+
Corrección de errores no relacionados
~~~

Preferir cambios pequeños y trazables.

Esto facilita:

- Revisiones de código.
- Identificación de errores.
- Reversión de cambios.
- Comprensión del historial.
- Trabajo colaborativo.

### Antes de finalizar una tarea

Antes de crear el Pull Request, verificar:

~~~bash
git status
~~~

Revisar los cambios:

~~~bash
git diff
~~~

Verificar que el proyecto compile correctamente.

Comprobar los servicios Docker:

~~~bash
docker compose -f docker-compose.dev.yml ps
~~~

Ejecutar las pruebas disponibles y realizar las validaciones correspondientes a la funcionalidad modificada.

### Regla general

Cuando exista una duda sobre dónde colocar una nueva funcionalidad, no crear inmediatamente una nueva estructura.

Primero:

1. Revisar cómo está implementada una funcionalidad similar.
2. Identificar la capa correspondiente.
3. Reutilizar las abstracciones existentes cuando sea posible.
4. Mantener la estructura actual del proyecto.
5. Crear nuevas abstracciones únicamente cuando exista una necesidad real.

## 11. Base de datos y migraciones

XKALA System utiliza **MySQL** como sistema gestor de base de datos y **Alembic** para controlar la evolución del esquema.

La estructura de la base de datos no debe modificarse directamente en producción mediante cambios manuales.

Los cambios estructurales deben quedar representados mediante migraciones.

### Base de datos

La configuración principal de desarrollo utiliza:

~~~text
Host: localhost
Port: 3307
Database: xkala_system
User: root
~~~

Desde los contenedores Docker, el Backend utiliza:

~~~text
Host: mysql
Port: 3306
Database: xkala_system
~~~

La diferencia de puertos se debe a la configuración de Docker:

~~~text
Equipo local
localhost:3307
      │
      ▼
Docker MySQL
3306
~~~

### Alembic

Las migraciones se encuentran en:

~~~text
back/alembic/versions/
~~~

Cada migración representa un cambio específico realizado sobre el esquema de la base de datos.

Ejemplo:

~~~text
back/alembic/
│
├── env.py
├── alembic.ini
└── versions/
    ├── ...
    ├── migration_1.py
    ├── migration_2.py
    └── migration_3.py
~~~

### Consultar el estado de las migraciones

Desde el Backend:

~~~bash
cd back
alembic current
~~~

Este comando muestra la revisión actualmente aplicada a la base de datos.

Para consultar el historial:

~~~bash
alembic history
~~~

Para consultar el historial detallado:

~~~bash
alembic history --verbose
~~~

### Crear una migración

Cuando se modifica la estructura de la base de datos, debe crearse una nueva migración.

Ejemplo:

~~~bash
alembic revision -m "add employee contract fields"
~~~

Esto genera un nuevo archivo dentro de:

~~~text
back/alembic/versions/
~~~

La migración debe contener explícitamente los cambios necesarios en `upgrade()` y, cuando corresponda, su operación inversa en `downgrade()`.

Ejemplo conceptual:

~~~python
def upgrade():
    # aplicar cambio
    pass


def downgrade():
    # revertir cambio
    pass
~~~

### Aplicar migraciones

Para aplicar todas las migraciones pendientes:

~~~bash
alembic upgrade head
~~~

Para ejecutar una migración dentro del entorno Docker:

~~~bash
docker exec -it xkala_backend alembic upgrade head
~~~

### Crear una migración a partir de los modelos

Si el proyecto utiliza generación automática de diferencias, puede utilizarse:

~~~bash
alembic revision --autogenerate -m "description of change"
~~~

Sin embargo, una migración generada automáticamente debe revisarse antes de ejecutarla.

No se debe asumir que Alembic siempre interpreta correctamente todos los cambios realizados en los modelos.

### Regla importante

Modificar un modelo SQLAlchemy **no modifica automáticamente la base de datos existente**.

Por ejemplo:

~~~text
SQLAlchemy Model
       │
       │ cambio
       ▼
Alembic Migration
       │
       │ upgrade
       ▼
MySQL
~~~

Por esta razón, cualquier cambio estructural debe considerar tanto el modelo como su migración correspondiente.

### Seeds

El proyecto utiliza seeders para insertar datos iniciales o datos necesarios para el funcionamiento del sistema.

Los seeders se encuentran en:

~~~text
back/app/infrastructure/database/seeds/
~~~

El proceso principal se ejecuta mediante:

~~~bash
python -m app.infrastructure.database.seeds.run_seeds
~~~

Dentro del entorno Docker:

~~~bash
docker exec -it xkala_backend \
python -m app.infrastructure.database.seeds.run_seeds
~~~

### Seeds y desarrollo

Los seeders deben diseñarse de forma que puedan ejecutarse nuevamente sin generar registros duplicados cuando el dato ya exista.

Esto es especialmente importante para datos como:

- Roles.
- Permisos.
- Tipos de documento.
- Usuarios iniciales.
- Catálogos del sistema.

El código del seed debe validar la existencia del registro cuando corresponda antes de intentar insertarlo nuevamente.

### Inicio automático del Backend

El entorno Docker ejecuta automáticamente las migraciones y los seeders mediante:

~~~text
back/start.sh
~~~

El flujo de inicio es:

~~~text
Backend inicia
     │
     ▼
Espera disponibilidad de MySQL
     │
     ▼
alembic upgrade head
     │
     ▼
Ejecuta seeds
     │
     ▼
Inicia Uvicorn
~~~

Por esta razón, normalmente no es necesario ejecutar manualmente las migraciones y seeds cada vez que se levanta el entorno Docker.

### Cambios de base de datos durante una funcionalidad

Cuando una nueva funcionalidad requiere modificar la base de datos, el cambio debe seguir este flujo:

~~~text
Modificar modelo
      │
      ▼
Crear migración
      │
      ▼
Revisar migración
      │
      ▼
Aplicar migración
      │
      ▼
Actualizar seed si corresponde
      │
      ▼
Probar funcionalidad
~~~

### Buenas prácticas

No realizar cambios manuales sobre la estructura de la base de datos para solucionar problemas que deberían resolverse mediante una migración.

Evitar eliminar tablas o columnas directamente durante el desarrollo sin entender las relaciones y migraciones existentes.

Antes de modificar una tabla:

1. Revisar el modelo SQLAlchemy.
2. Revisar las migraciones relacionadas.
3. Revisar las relaciones con otras tablas.
4. Crear la migración correspondiente.
5. Aplicar la migración en desarrollo.
6. Probar la funcionalidad.
7. Incluir la migración en el commit correspondiente.

### Regla principal

La base de datos debe poder reconstruirse y evolucionar de forma controlada utilizando:

~~~text
Alembic
+
Models SQLAlchemy
+
Seeds
~~~

Los cambios estructurales deben quedar registrados en Git mediante sus respectivas migraciones.

## 12. Testing y validación

XKALA System debe validarse antes de integrar cambios en `main`.

El objetivo es detectar errores antes de crear el Pull Request y asegurar que una modificación no afecte funcionalidades existentes.

### Tipos de validación

Las validaciones del proyecto se pueden dividir en:

- Validación del Backend.
- Validación del Frontend.
- Validación de la API.
- Validación de integración.
- Validación del entorno Docker.

### Backend

Antes de finalizar una modificación en el Backend, comprobar que la aplicación inicia correctamente.

Verificar el estado de los contenedores:

~~~bash
docker compose -f docker-compose.dev.yml ps
~~~

Revisar los logs del Backend:

~~~bash
docker logs xkala_backend
~~~

El Backend debe iniciar correctamente y Uvicorn debe quedar ejecutándose en:

~~~text
http://localhost:8000
~~~

### Swagger / OpenAPI

La API dispone de documentación interactiva mediante Swagger.

En el entorno DEV:

~~~text
http://localhost:8000/docs
~~~

También puede utilizarse el esquema OpenAPI:

~~~text
http://localhost:8000/openapi.json
~~~

Swagger debe utilizarse para validar rápidamente:

- Rutas disponibles.
- Métodos HTTP.
- Parámetros.
- Schemas.
- Respuestas.
- Requisitos de autenticación.

### Validación de endpoints

Cuando se modifica un endpoint, se debe probar como mínimo:

1. Caso exitoso.
2. Datos inválidos.
3. Recurso inexistente cuando corresponda.
4. Usuario no autenticado cuando corresponda.
5. Usuario sin permisos cuando corresponda.
6. Casos límite relevantes.

Ejemplo de flujo de autenticación:

~~~text
Login
  │
  ▼
Access Token
  │
  ▼
Endpoint protegido
  │
  ├── Token válido ──────► 200
  │
  ├── Token inválido ────► Error de autenticación
  │
  └── Sin permiso ───────► Error de autorización
~~~

### Frontend

Antes de finalizar una modificación en Angular, comprobar que la aplicación compile correctamente.

Dentro del contenedor:

~~~bash
docker exec -it xkala_frontend npm run build
~~~

También puede verificarse el desarrollo mediante:

~~~text
http://localhost:4200
~~~

Las funcionalidades modificadas deben probarse directamente desde la interfaz.

### Validación de comunicación Frontend → Backend

Cuando una funcionalidad utiliza la API, comprobar que la petición realmente llega al Backend.

En desarrollo, las peticiones utilizan:

~~~text
/api
~~~

El flujo esperado es:

~~~text
Frontend
   │
   │ /api/...
   ▼
Angular Dev Server
   │
   │ Proxy
   ▼
FastAPI
   │
   ▼
MySQL
~~~

Si una petición devuelve `404`, `401`, `403`, `422` o `500`, revisar primero:

- URL utilizada.
- Método HTTP.
- Proxy de Angular.
- Ruta registrada en FastAPI.
- Schema enviado.
- Autenticación.
- Permisos.
- Logs del Backend.

### Validación de Docker

Después de modificar Docker, configuración de entornos o dependencias, reconstruir el entorno:

~~~bash
docker compose -f docker-compose.dev.yml up --build
~~~

Verificar posteriormente:

~~~bash
docker compose -f docker-compose.dev.yml ps
~~~

Todos los servicios requeridos deben encontrarse en estado operativo.

### Logs

Cuando un servicio no funcione correctamente, revisar primero sus logs.

Backend:

~~~bash
docker logs xkala_backend
~~~

Frontend:

~~~bash
docker logs xkala_frontend
~~~

MySQL:

~~~bash
docker logs xkala_mysql
~~~

Para seguir los logs en tiempo real:

~~~bash
docker logs -f xkala_backend
~~~

### Validación de una funcionalidad

Una funcionalidad no debe considerarse terminada únicamente porque el código compile.

El flujo recomendado es:

~~~text
Implementar
    │
    ▼
Compilar
    │
    ▼
Levantar Docker
    │
    ▼
Probar API
    │
    ▼
Probar interfaz
    │
    ▼
Revisar errores
    │
    ▼
Validar casos límite
    │
    ▼
Revisar Git
    │
    ▼
Commit
~~~

### Checklist antes del Pull Request

Antes de crear un Pull Request:

~~~text
[ ] El código compila correctamente
[ ] Docker inicia correctamente
[ ] Las migraciones necesarias fueron creadas
[ ] Los seeds funcionan correctamente cuando fueron modificados
[ ] Los endpoints afectados fueron probados
[ ] La interfaz afectada fue probada
[ ] Se validaron errores y casos límite
[ ] No existen secretos incluidos en el código
[ ] No existen archivos innecesarios en el commit
[ ] La documentación fue actualizada si corresponde
[ ] Los cambios fueron revisados con git diff
~~~

### Regla principal

Una tarea se considera lista para revisión cuando no solamente funciona en el caso esperado, sino que también se ha comprobado su comportamiento ante errores y condiciones relevantes.

La validación debe realizarse sobre el entorno DEV antes de integrar el cambio en `main`.

## 13. Seguridad y autenticación

XKALA System implementa mecanismos de autenticación, autorización y auditoría para proteger los recursos del sistema.

La seguridad se encuentra principalmente distribuida entre:

~~~text
back/app/core/security/
back/app/core/exceptions/
back/app/core/dependencies/
back/app/infrastructure/
~~~

### Autenticación

La autenticación utiliza **JWT (JSON Web Token)**.

El usuario inicia sesión utilizando su número de documento y contraseña.

Flujo:

~~~text
Usuario
   │
   │ número de documento + password
   ▼
POST /auth/login
   │
   ▼
LoginUserUseCase
   │
   ├──► Buscar usuario
   │
   ├──► Verificar contraseña
   │
   ├──► Verificar estado
   │
   └──► Generar tokens
          │
          ├──► Access Token
          └──► Refresh Token
~~~

El endpoint de autenticación es:

~~~text
POST /auth/login
~~~

### Contraseñas

Las contraseñas no deben almacenarse en texto plano.

El sistema utiliza hashing mediante `bcrypt`.

El valor almacenado en la base de datos corresponde al hash de la contraseña y no a la contraseña original.

El proceso conceptual es:

~~~text
Password
   │
   ▼
PasswordHasher
   │
   ▼
bcrypt
   │
   ▼
Password Hash
   │
   ▼
Database
~~~

Para validar una contraseña durante el login, el sistema compara la contraseña proporcionada con el hash almacenado.

### Access Token

El Access Token se utiliza para acceder a endpoints protegidos.

Las peticiones autenticadas deben enviar el token mediante:

~~~text
Authorization: Bearer <access_token>
~~~

El token contiene información necesaria para identificar al usuario y su rol.

### Refresh Token

El Refresh Token permite obtener un nuevo Access Token cuando este expira.

El endpoint correspondiente es:

~~~text
POST /auth/refresh
~~~

El Refresh Token debe tratarse como información sensible y no debe exponerse innecesariamente.

### Autorización

La autenticación determina quién es el usuario.

La autorización determina qué puede hacer ese usuario.

XKALA utiliza **RBAC (Role-Based Access Control)**.

El flujo general es:

~~~text
Usuario
   │
   ▼
Rol
   │
   ▼
Permisos
   │
   ▼
Endpoint protegido
~~~

Ejemplo:

~~~text
Super Admin
     │
     ├── create_user
     ├── update_user
     ├── view_users
     ├── upload_documents
     └── delete_documents
~~~

### Protección mediante permisos

Los endpoints que requieren un permiso específico deben utilizar el mecanismo de autorización definido por el Backend.

Ejemplo:

~~~python
Depends(require_permission("create_user"))
~~~

Esto permite evitar que cada endpoint implemente manualmente la lógica de autorización.

### Protección mediante roles

Cuando una operación debe estar limitada a un rol específico, puede utilizarse el mecanismo de autorización por rol.

Ejemplo:

~~~python
Depends(require_role("Super Admin"))
~~~

La elección entre permiso y rol debe realizarse de acuerdo con la responsabilidad de la operación.

Cuando una funcionalidad representa una capacidad concreta del sistema, se recomienda utilizar permisos.

### Usuario activo

Además de validar las credenciales, el sistema verifica el estado del usuario.

Un usuario inactivo no debe poder autenticarse correctamente aunque la contraseña proporcionada sea válida.

Flujo:

~~~text
Credenciales
    │
    ▼
Usuario existe
    │
    ▼
Password válida
    │
    ▼
Usuario activo
    │
    ▼
Generar tokens
~~~

### Auditoría

El sistema registra información relacionada con las operaciones realizadas sobre la API.

La auditoría puede incluir información como:

- Usuario.
- Endpoint.
- Método HTTP.
- Dirección IP.
- User Agent.
- Código de respuesta.
- Acción realizada.
- Descripción.
- Información adicional.

El objetivo es permitir rastrear operaciones importantes realizadas dentro del sistema.

### Excepciones de seguridad

Los errores relacionados con autenticación y autorización deben utilizar las excepciones definidas por el sistema.

Ejemplos:

~~~text
Credenciales inválidas
Usuario inactivo
Token inválido
Token expirado
Permiso insuficiente
~~~

Las respuestas de error deben mantener el formato estándar utilizado por la API.

### Secretos y configuración

Las claves utilizadas para JWT y otras configuraciones sensibles deben mantenerse mediante variables de entorno.

No se deben almacenar secretos reales directamente en:

~~~text
Código fuente
Commits
README
Documentación pública
Archivos de configuración versionados
~~~

Los entornos utilizan configuraciones independientes:

~~~text
back/.env.dev
back/.env.prod
~~~

### Reglas de seguridad para desarrolladores

Los desarrolladores deben:

1. No almacenar contraseñas en texto plano.
2. No registrar contraseñas en logs.
3. No incluir tokens en commits.
4. No incluir claves privadas en el código.
5. No desactivar autenticación para facilitar pruebas sin una razón justificada.
6. No eliminar validaciones de permisos para solucionar temporalmente un problema.
7. Mantener separadas las configuraciones DEV y PROD.
8. Revisar cualquier cambio relacionado con autenticación y autorización antes de integrarlo.

### Regla principal

La seguridad debe considerarse parte de la funcionalidad y no una etapa posterior.

Cualquier cambio relacionado con usuarios, roles, permisos, autenticación, archivos o información sensible debe revisar explícitamente sus implicaciones de seguridad antes de integrarse en `main`.


## 14. Documentación de API

XKALA System expone una API REST desarrollada con FastAPI.

La documentación de la API se genera automáticamente mediante OpenAPI y puede consultarse utilizando Swagger UI.

### Swagger

En el entorno DEV:

~~~text
http://localhost:8000/docs
~~~

Swagger permite consultar y probar los endpoints disponibles directamente desde el navegador.

### OpenAPI

El esquema OpenAPI está disponible en:

~~~text
http://localhost:8000/openapi.json
~~~

Este esquema representa la definición actual de la API y puede utilizarse para consultar:

- Endpoints.
- Métodos HTTP.
- Parámetros.
- Schemas de entrada.
- Schemas de respuesta.
- Autenticación.
- Códigos de respuesta.

### Organización de endpoints

Las rutas de la API se encuentran organizadas por dominio o funcionalidad dentro de:

~~~text
back/app/interfaces/api/
~~~

Ejemplo:

~~~text
back/app/interfaces/api/
│
├── auth/
├── user/
├── role/
├── permission/
├── city/
├── document_type/
├── hr/
└── dashboard/
~~~

Cada módulo debe mantener sus rutas relacionadas agrupadas dentro de su propio espacio.

### Schemas

Los schemas utilizados para validar las peticiones y respuestas se encuentran principalmente en:

~~~text
back/app/interfaces/schemas/
~~~

Los schemas permiten definir la estructura esperada de los datos recibidos por la API.

Ejemplo conceptual:

~~~text
HTTP Request
     │
     ▼
Pydantic Schema
     │
     ▼
Route
     │
     ▼
Use Case
~~~

La validación de entrada debe realizarse mediante los mecanismos establecidos por FastAPI y Pydantic.

### Autenticación en Swagger

Los endpoints protegidos requieren autenticación.

Cuando Swagger lo permita, se debe utilizar el mecanismo de autenticación configurado para enviar:

~~~text
Authorization: Bearer <access_token>
~~~

El flujo recomendado para probar endpoints protegidos es:

~~~text
POST /auth/login
       │
       ▼
Access Token
       │
       ▼
Authorize
       │
       ▼
Endpoint protegido
~~~

### Prueba de endpoints

Cuando se desarrolla o modifica un endpoint, se recomienda validarlo inicialmente desde Swagger antes de probarlo desde el Frontend.

Esto permite determinar si un problema pertenece al Backend o a la comunicación Frontend → Backend.

Orden recomendado:

~~~text
Swagger
   │
   ▼
Backend
   │
   ▼
Proxy / API
   │
   ▼
Frontend
~~~

### Documentación adicional

La documentación específica de funcionalidades de la API puede mantenerse dentro de:

~~~text
docs/api/
~~~

Actualmente esta documentación puede incluir información específica sobre determinados módulos o recursos.

Ejemplo:

~~~text
docs/api/users.md
~~~

### Cambios en la API

Cuando un cambio modifica el comportamiento público de un endpoint, se debe revisar si también es necesario actualizar la documentación correspondiente.

Esto incluye cambios como:

- Crear nuevos endpoints.
- Eliminar endpoints.
- Cambiar métodos HTTP.
- Modificar parámetros.
- Modificar request schemas.
- Modificar response schemas.
- Cambiar códigos de respuesta.
- Agregar requisitos de autenticación.
- Agregar requisitos de permisos.

### Compatibilidad

Antes de modificar un endpoint existente, verificar si el Frontend u otros módulos dependen de él.

No se debe cambiar silenciosamente:

~~~text
URL
Método HTTP
Nombre de campos
Estructura de respuesta
Requisitos de autenticación
Permisos
~~~

sin revisar primero los consumidores de la API.

### Regla principal

La documentación de la API debe mantenerse alineada con el comportamiento real del Backend.

Si el código cambia y la documentación deja de representar el comportamiento real de la API, la documentación debe actualizarse como parte de la misma tarea.

## 15. Checklist para nuevos desarrolladores

Antes de comenzar a desarrollar en XKALA System, un nuevo integrante debe completar las siguientes verificaciones.

### 15.1 Preparación del entorno

Verificar que las herramientas necesarias estén instaladas:

~~~bash
git --version
docker --version
docker compose version
node --version
npm --version
python3 --version
~~~

### 15.2 Obtener el proyecto

Clonar el repositorio:

~~~bash
git clone <https://github.com/Xkala-SAS/xkala-system>
cd xkala-system
~~~

Verificar el estado inicial:

~~~bash
git status
~~~

La rama principal debe encontrarse limpia antes de comenzar una nueva tarea.

### 15.3 Levantar el entorno DEV

Ejecutar:

~~~bash
docker compose -f docker-compose.dev.yml up --build
~~~

O ejecutar en segundo plano:

~~~bash
docker compose -f docker-compose.dev.yml up --build -d
~~~

Verificar los servicios:

~~~bash
docker compose -f docker-compose.dev.yml ps
~~~

### 15.4 Verificar los servicios

Comprobar el Frontend:

~~~text
http://localhost:4200
~~~

Comprobar el Backend:

~~~text
http://localhost:8000
~~~

Comprobar Swagger:

~~~text
http://localhost:8000/docs
~~~

Comprobar que MySQL esté disponible:

~~~text
Host: localhost
Port: 3307
Database: xkala_system
~~~

### 15.5 Verificar autenticación

Realizar un login mediante Swagger o utilizando el Frontend.

Verificar que:

~~~text
Login
   │
   ▼
Access Token
   │
   ▼
Endpoint protegido
~~~

funcione correctamente.

Las credenciales de desarrollo deben obtenerse de la configuración o documentación interna correspondiente y nunca deben copiarse desde credenciales reales de producción.

### 15.6 Revisar la arquitectura

Antes de desarrollar una nueva funcionalidad, revisar:

~~~text
docs/architecture/hexagonal.md
docs/development/setup.md
~~~

Identificar:

- Dominio afectado.
- Capa correspondiente.
- Casos de uso existentes.
- Servicios existentes.
- Repositorios existentes.
- Componentes reutilizables.

No comenzar creando archivos nuevos sin revisar primero cómo está organizada la funcionalidad existente.

### 15.7 Crear la rama de trabajo

Actualizar `main`:

~~~bash
git checkout main
git pull origin main
~~~

Crear una rama:

~~~bash
git checkout -b feature/nombre-de-la-funcionalidad
~~~

La rama debe representar una tarea concreta.

### 15.8 Desarrollar

Durante el desarrollo:

- Mantener la arquitectura existente.
- Evitar duplicar lógica.
- Mantener responsabilidades separadas.
- No modificar producción para solucionar problemas de desarrollo.
- No incluir secretos en el código.
- Crear migraciones cuando se modifique la estructura de la base de datos.
- Actualizar la documentación cuando corresponda.

### 15.9 Validar

Antes de crear el Pull Request:

~~~bash
git status
~~~

Revisar los cambios:

~~~bash
git diff
~~~

Verificar Docker:

~~~bash
docker compose -f docker-compose.dev.yml ps
~~~

Revisar los logs si es necesario:

~~~bash
docker logs xkala_backend
docker logs xkala_frontend
docker logs xkala_mysql
~~~

Probar la funcionalidad modificada desde la API y/o el Frontend según corresponda.

### 15.10 Crear el commit

El commit debe seguir la convención establecida:

~~~text
tipo(alcance): descripción
~~~

Ejemplo:

~~~bash
git add .
git commit -m "feat(users): add employee registration"
~~~

Antes del commit, asegurarse de que no se estén incluyendo:

- `.env` con secretos.
- Archivos temporales.
- Archivos generados innecesariamente.
- Cambios no relacionados con la tarea.

### 15.11 Actualizar la rama

Antes de crear el Pull Request:

~~~bash
git checkout main
git pull origin main

git checkout feature/nombre-de-la-funcionalidad
git merge main
~~~

Resolver cualquier conflicto y volver a validar el proyecto.

### 15.12 Crear Pull Request

El Pull Request debe incluir:

- Descripción del cambio.
- Motivo de la implementación.
- Funcionalidades afectadas.
- Pruebas realizadas.
- Migraciones realizadas, si aplica.
- Cambios relevantes de configuración, si aplica.
- Consideraciones o riesgos conocidos.

### 15.13 Checklist final

Antes de solicitar revisión:

~~~text
[ ] Entorno DEV funcionando
[ ] Código compilando correctamente
[ ] Backend funcionando
[ ] Frontend funcionando
[ ] API validada
[ ] Autenticación validada cuando corresponde
[ ] Permisos validados cuando corresponde
[ ] Migraciones creadas cuando corresponde
[ ] Seeds actualizados cuando corresponde
[ ] Tests ejecutados cuando corresponda
[ ] Documentación actualizada cuando corresponde
[ ] Sin secretos en los cambios
[ ] Sin archivos innecesarios
[ ] Git diff revisado
[ ] Commit siguiendo la convención
[ ] Rama actualizada con main
[ ] Pull Request preparado
~~~

### 15.14 Regla de incorporación

Un desarrollador nuevo debe poder completar este checklist y levantar el proyecto sin modificar arbitrariamente la arquitectura existente.

Si durante la incorporación surge una duda sobre la estructura, configuración o flujo de trabajo, primero se debe consultar la documentación existente y revisar implementaciones similares antes de introducir una nueva solución.

La documentación del proyecto debe mantenerse actualizada para que este proceso pueda repetirse con nuevos integrantes.