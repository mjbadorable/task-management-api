# Task Management API

A RESTful backend API for managing tasks built with **FastAPI** and **SQLAlchemy**.

This project demonstrates how to build a production-style backend service with proper project structure, database integration, environment configuration, and full CRUD operations.

---

# Features

* Create tasks
* Retrieve all tasks
* Retrieve a specific task
* Update tasks
* Delete tasks
* Persistent database storage
* Environment configuration using `.env`
* Automatic API documentation

---

# Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Programming language            |
| FastAPI       | Backend web framework           |
| Uvicorn       | ASGI server                     |
| SQLAlchemy    | ORM for database operations     |
| SQLite        | Local database                  |
| python-dotenv | Environment variable management |
| Git           | Version control                 |

---

# Project Structure

```
task-management-api/
│
├── app/
│   ├── main.py          # Application entry point
│   ├── database.py      # Database configuration
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database operations
│   └── routers/
│       └── tasks.py     # Task API routes
│
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md
```

---

# Installation

Clone the repository

```
git clone https://github.com/YOUR_USERNAME/task-management-api.git
cd task-management-api
```

---

# Create Virtual Environment

```
python -m venv venv
```

Activate it

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

# Install Dependencies

```
pip install -r requirements.txt
```

---

# Environment Configuration

Create a `.env` file in the project root.

Example:

```
DATABASE_URL=sqlite:///./tasks.db
```

---

# Run the API

Start the server:

```
uvicorn app.main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

---

# Interactive API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

Alternative documentation:

```
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

## Create Task

POST `/tasks`

Request body:

```
{
 "title": "Learn FastAPI"
}
```

---

## Get All Tasks

GET `/tasks`

Example response:

```
[
 {
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
 }
]
```

---

## Get Task by ID

GET `/tasks/{id}`

Example:

```
GET /tasks/1
```

---

## Update Task

PUT `/tasks/{id}`

Example parameters:

```
title = Updated task
completed = true
```

---

## Delete Task

DELETE `/tasks/{id}`

Example:

```
DELETE /tasks/1
```

---

# Development Workflow

Typical development process:

```
git add .
git commit -m "describe your change"
git push
```

---

# Future Improvements

Planned improvements for this project:

* User authentication with JWT
* Task ownership (users manage their own tasks)
* Database migrations
* Docker containerization
* Automated testing
* Deployment to cloud

---

# Learning Goals

This project is part of a backend development learning path covering:

* REST API design
* Backend architecture
* Database integration
* Version control
* Environment configuration
* API documentation

---

# Author

Marvin Jhay Adorable

Backend development learning project.
