# 🚀 Mentoria API — Django REST + PostgreSQL + Docker

**Mentoria API** is a backend application built with **Django 5**, **Django REST Framework**, and **PostgreSQL**, fully containerized using **Docker**.  
It provides a solid foundation for building modern, scalable APIs with automatic documentation using **Swagger** and **Redoc**.

---

## 📚 Technologies Used

- **Python 3.13**
- **Django 5**
- **Django REST Framework**
- **PostgreSQL 15**
- **Docker & Docker Compose**
- **DRF Spectacular** (OpenAPI 3 + Swagger + Redoc)

---

## 🏗️ Architecture

```
.
├── api/                          # API project
├── mentoria_api/                 # Main Django application
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Copy environment variables file

```sh
cp .env.example .env
```

Edit the variables as needed.

---

### 2️⃣ Build and run containers

```sh
docker-compose up --build
```

The API will be available at:

```
http://localhost:8000/
```

---

## 📘 API Documentation

After starting the containers, access:

| Type             | URL                                       |
| ---------------- | ----------------------------------------- |
| **Swagger UI**   | http://localhost:8000/api/schema/swagger/ |
| **Redoc**        | http://localhost:8000/api/schema/redoc/   |
| **OpenAPI JSON** | http://localhost:8000/api/schema/         |

---

## 🧪 Run Tests

```sh
docker-compose exec web pytest
```

or:

```sh
docker exec -it mentoria_web pytest
```

---

## 🛠️ Make Migrations

```sh
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

---

## 🧑‍💻 Access Django Shell

```sh
docker-compose exec web python manage.py shell
```

---

## 🐳 Access Container Bash

```sh
docker exec -it mentoria_web bash
```

_(You will enter as `appuser` with host UID/GID.)_

---

## 📦 Install New Packages

1. Edit **requirements.txt**

2. Rebuild the container:

```sh
docker-compose build web
docker-compose up
```

---

## 📝 Conventions

- Python code following **PEP8**
- Commits following **Conventional Commits**
- Fully isolated environment using Docker

---

## 🤝 Contributions

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the **MIT License**.
