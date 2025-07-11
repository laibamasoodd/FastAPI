# 🚀 FastAPI Backend Project

A high-performance, easy-to-extend backend API built with [FastAPI](https://fastapi.tiangolo.com/).  
This project supports JWT authentication, SQLAlchemy ORM, Alembic migrations, and PostgreSQL database.

---

## 📦 Tech Stack

- ⚙️ **FastAPI** – lightning-fast Python web framework
- 🐘 **PostgreSQL** – relational database
- 🧰 **SQLAlchemy** – ORM for DB models and queries
- 🧬 **Alembic** – schema migrations
- 🔒 **JWT Auth** – secure user authentication
- 📄 **Pydantic** – data validation using type hints
- 🐳 **Docker** – for containerized deployment

---

## 📁 Project Structure
.
├── app/
│   ├── main.py              # Entry point
│   ├── models.py              # SQLAlchemy models
│   ├── routes/              # API route definitions
│   ├── schemas.py             # Pydantic schemas (request/response validation)
│   ├── database.py          # Database connection setup
│   └── oauth2.py                # JWT handling, password hashing
├── alembic/                 # Alembic migration files
├── alembic.ini              # Alembic config file
├── .env                     # Environment variables
├── requirements.txt         # Project dependencies
└── README.md

