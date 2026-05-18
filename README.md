# Capstone Backend (FastAPI + MySQL + Docker)

A backend service built with **FastAPI**, **MySQL**, and **Docker Compose** for easy setup and deployment.

---

## 🚀 Tech Stack
- Python 3.12
- FastAPI
- MySQL 8.0
- Poetry
- Docker & Docker Compose

---

## 📦 Run the Project

### 1. Clone repo
```bash
git clone <repo-url>
cd <project-folder>
```

### 2. Running the code
```bash
docker compose up --build
```
### 2. Accessing the App
API: http://localhost:8000

Docs: http://localhost:8000/docs

### 3. Stopping the project
```bash
docker compose down

# to reset the DB
docker compose down -v
```