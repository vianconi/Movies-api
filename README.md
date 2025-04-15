
# Movie API

Una API construida con Django y Django REST Framework (DRF) para gestionar películas, calificaciones y usuarios.

## Requisitos

- Python 3.8+
- Django 5.2
- Django REST Framework
- PostgreSQL
- drf_yasg (para Swagger UI)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/movie-api.git
   cd movie-api
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa 'venv\Scripts\Activate'
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno en un archivo `.env`:
   ```env
   SECRET_KEY='tu_secreto'
   DB_NAME='nombre_base_datos'
   DB_USER='usuario'
   DB_PASSWORD='contraseña'
   DB_HOST='localhost'
   DB_PORT='5432'
   ```

5. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```

6. Crea un superusuario para acceder al admin:
   ```bash
   python manage.py createsuperuser
   ```

7. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```

## Endpoints

### Autenticación

- **Obtener token JWT**:  
  `POST /user/token/`  
  Parámetros:  
  ```json
  {
    "username": "usuario",
    "password": "contraseña"
  }
  ```

- **Refrescar token JWT**:  
  `POST /user/token/refresh/`  
  Parámetros:  
  ```json
  {
    "refresh": "tu_refresh_token"
  }
  ```

### Películas

- **Listar todas las películas**:  
  `GET /movie/`  
  Respuesta:
  ```json
  [
    {
      "id": 1,
      "title": "Inception",
      "release_date": "2010-07-16",
      "duration": 148,
      "synopsis": "A thief who enters the minds of others through their dreams..."
    },
    ...
  ]
  ```

- **Crear nueva película**:  
  `POST /movie/`  
  Parámetros:
  ```json
  {
    "title": "Inception",
    "release_date": "2010-07-16",
    "duration": 148,
    "synopsis": "A thief who enters the minds of others through their dreams..."
  }
  ```

- **Actualizar película**:  
  `PUT /movie/<int:pk>/`  
  Parámetros:
  ```json
  {
    "title": "Updated Inception",
    "release_date": "2010-07-16",
    "duration": 148,
    "synopsis": "Updated synopsis"
  }
  ```

### Calificaciones de Películas

- **Listar calificaciones de usuario**:  
  `GET /user/rate/`  
  Respuesta:
  ```json
  [
    {
      "id": 1,
      "rating": 5,
      "user": 1,
      "movie": 1
    },
    ...
  ]
  ```

- **Crear calificación**:  
  `POST /user/rate/`  
  Parámetros:
  ```json
  {
    "user": 1,
    "movie": 1,
    "rating": 5
  }
  ```

## Swagger UI

Para explorar los endpoints de manera interactiva, visita:  
`http://localhost:8000/swagger/`

## Estructura del Proyecto

```
movie-api/
├── core/                # Configuración global de Django
│   ├── settings.py      # Configuración del proyecto
│   ├── urls.py          # URLs globales
│   └── wsgi.py
├── movie/               # App para gestionar las películas
│   ├── models.py        # Modelos de película
│   ├── serializers.py   # Serializadores de película
│   ├── urls.py          # Rutas de la app de películas
│   ├── views.py         # Vistas relacionadas a películas
│   └── migrations/
├── user/                # App para gestionar usuarios y calificaciones
│   ├── models.py        # Modelos de usuario y calificación
│   ├── serializers.py   # Serializadores de calificación
│   ├── urls.py          # Rutas de la app de usuarios
│   ├── views.py         # Vistas relacionadas a calificaciones
│   └── migrations/
└── manage.py            # Herramienta de gestión de Django
```

## Contribuciones

Las contribuciones son bienvenidas. Para hacerlo, por favor crea un fork del repositorio y abre un Pull Request.

---

¡Disfruta usando la Movie API! 🎬
