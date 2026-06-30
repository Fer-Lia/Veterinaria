# 🐾 API Veterinaria

API REST para la gestión de una clínica veterinaria: clientes, mascotas y veterinarios. 

## 📋 Descripción

Esta API permite gestionar el ciclo completo de información de una veterinaria:

- **Clientes**: registro y administración de los propietarios de las mascotas.
- **Mascotas**: registro de mascotas vinculadas a un cliente, con relación de clave foránea.
- **Veterinarios**: registro del personal veterinario y su especialidad.

Cada entidad implementa un CRUD completo (crear, leer, actualizar, eliminar) siguiendo una arquitectura en capas, con validación de datos, manejo de errores y migraciones de base de datos versionadas.

## 🛠️ Stack tecnológico

| Tecnología | Uso en el proyecto |
|---|---|
| [Python 3.14](https://www.python.org/) | Lenguaje principal |
| [FastAPI](https://fastapi.tiangolo.com/) | Framework para la construcción de la API REST |
| [Uvicorn](https://www.uvicorn.org/) | Servidor ASGI que ejecuta la aplicación |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM para el mapeo objeto-relacional con PostgreSQL |
| [PostgreSQL](https://www.postgresql.org/) | Sistema gestor de base de datos relacional |
| [psycopg2](https://www.psycopg.org/) | Driver de conexión entre SQLAlchemy y PostgreSQL |
| [Pydantic](https://docs.pydantic.dev/) / [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) | Validación de datos y gestión de variables de entorno |
| [Alembic](https://alembic.sqlalchemy.org/) | Migraciones de base de datos versionadas |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Carga de variables de entorno desde `.env` |
| [email-validator](https://pypi.org/project/email-validator/) | Validación de formato de direcciones de correo |

## 🏗️ Arquitectura

El proyecto sigue una **arquitectura en capas**, separando responsabilidades para facilitar el mantenimiento y la escalabilidad:

```
app/
├── main.py              # Punto de entrada: instancia FastAPI e incluye los routers
├── config/
│   └── settings.py      # Configuración y variables de entorno (Pydantic Settings)
├── db/
│   └── database.py       # Motor de conexión, sesión y Base declarativa de SQLAlchemy
├── models/                # Definición de las tablas (SQLAlchemy)
│   ├── cliente.py
│   ├── mascota.py
│   └── veterinario.py
├── schemas/               # Validación de entrada/salida (Pydantic)
│   ├── cliente.py
│   ├── mascota.py
│   └── veterinario.py
├── routers/                # Endpoints HTTP (capa de presentación)
│   ├── cliente.py
│   ├── mascota.py
│   └── veterinario.py
└── services/                # Lógica de negocio
    ├── cliente.py
    ├── mascota.py
    └── veterinario.py
```

| Capa | Responsabilidad |
|---|---|
| **Router** | Recibe la petición HTTP y delega en el servicio correspondiente |
| **Schema** | Valida la forma de los datos de entrada y de salida |
| **Service** | Contiene la lógica de negocio y las operaciones contra la base de datos |
| **Model** | Define la estructura de las tablas en PostgreSQL |

### Relaciones entre entidades

- Un **Cliente** puede tener varias **Mascotas** (relación uno a muchos, mediante clave foránea `dni_cliente`).
- **Veterinario** es una entidad independiente.

## ⚙️ Instalación y configuración

### Requisitos previos

- Python 3.14+
- PostgreSQL instalado y en ejecución
- pgAdmin (opcional, recomendado para inspeccionar la base de datos)

### Pasos

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Fer-Lia/Veterinaria.git
   cd Veterinaria
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1   # Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Crea una base de datos en PostgreSQL llamada `veterinaria_db`.

5. Configura las variables de entorno: copia `.env.example` a `.env` y completa tus credenciales locales.
   ```bash
   DB_HOST=localhost
   DB_PORT=5432
   DB_USER=postgres
   DB_PASSWORD=tu_contraseña_aqui
   DB_NAME=veterinaria_db
   ```
   > ⚠️ El archivo `.env` nunca se sube al repositorio (está incluido en `.gitignore`). Cada persona del equipo configura el suyo con sus propias credenciales locales.

6. Aplica las migraciones de base de datos:
   ```bash
   alembic upgrade head
   ```

7. Arranca el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

8. Abre la documentación interactiva (Swagger UI) en:
   ```
   http://127.0.0.1:8000/docs
   ```

## 🔄 Migraciones de base de datos

El proyecto usa **Alembic** para gestionar cambios en el esquema de la base de datos sin pérdida de datos.

- Generar una nueva migración tras modificar un modelo:
  ```bash
  alembic revision --autogenerate -m "descripcion del cambio"
  ```
- Aplicar las migraciones pendientes:
  ```bash
  alembic upgrade head
  ```

## 🌳 Flujo de trabajo (GitFlow)

El desarrollo sigue la metodología **[GitFlow](https://davidregalado255.medium.com/what-is-gitflow-b3396770cd42)**:

- `master` → código estable, listo para producción.
- `develop` → rama de integración de funcionalidades.
- `feature/*` → una rama por funcionalidad concreta (ej. `feature/crud-mascotas`).

Cada funcionalidad se desarrolla en su propia rama, se fusiona en `develop` mediante un merge `--no-ff`, y los commits siguen la convención [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `chore:`, etc.).

## 📚 Documentación de la API

Una vez el servidor está en ejecución, FastAPI genera automáticamente:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## 👥 Autoras
**Irma Diaz** 
**Lia Fernández** 