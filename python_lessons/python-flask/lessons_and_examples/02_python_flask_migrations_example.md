# Guide to Flask-Migrate with MySQL

## Overview
Flask-Migrate is an extension that uses **Alembic** to handle database migrations in Flask applications. It allows you to create and apply database schema changes without manually altering the database.

This guide covers setting up Flask-Migrate, initializing migrations, creating and applying database schema changes.

---

## API Overview

### API Information
- **Title**: Flask-Migrate API
- **Description**: An API for managing users and posts, demonstrating database migrations and schema validation using Flask-Migrate and Flask-RESTx.
- **Version**: 1.0

### API Endpoints

#### 1. Users
- **`GET /users/`**: List all users.
- **`POST /users/`**: Create a new user.
- **`GET /users/<id>`**: Retrieve a user by ID.
- **`DELETE /users/<id>`**: Delete a user by ID.

#### 2. Posts
- **`GET /posts/`**: List all posts.
- **`POST /posts/`**: Create a new post.
- **`GET /posts/<id>`**: Retrieve a post by ID.
- **`DELETE /posts/<id>`**: Delete a post by ID.

### API Models

#### 1. User Model
- **`id`** *(Integer)*: Unique identifier of the user (read-only).
- **`username`** *(String)*: Username of the user (required, unique).
- **`email`** *(String)*: Email address of the user (required, unique).
- **`posts`** *(List of Posts)*: Posts authored by the user.

#### 2. Post Model
- **`id`** *(Integer)*: Unique identifier of the post (read-only).
- **`title`** *(String)*: Title of the post (required).
- **`content`** *(String)*: Content of the post (required).
- **`user_id`** *(Integer)*: Identifier of the author (required).

---

## Project Structure
```plaintext
pythonFlaskUserPosts/
├── app/
│   ├── __init__.py        # Initialize Flask app, database, and migrations
│   ├── models/            # Directory for SQLAlchemy models
│   │   ├── __init__.py    # SQLAlchemy instance
│   │   ├── user.py        # User model
│   │   └── post.py        # Post model
│   ├── schemas/           # Directory for API schemas
│   │   ├── __init__.py    # Initialize schemas
│   │   ├── user_schema.py # User schema
│   │   └── post_schema.py # Post schema
│   ├── routes/            # Directory for API routes
│   │   ├── __init__.py    # Register routes
│   │   ├── user_routes.py # User API routes
│   │   └── post_routes.py # Post API routes
├── migrations/            # Created by Flask-Migrate
├── .env                   # Environment variables
├── .venv/                 # Virtual environment directory
├── run.py                 # Entry point for running the app
├── requirements.txt       # Project dependencies
```

---

## Step 1: Setting Up the Environment

### Create Virtual Environment

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install flask flask-restx flask-sqlalchemy flask-migrate python-dotenv mysql-connector-python
   ```

3. Save dependencies:
   ```bash
   pip freeze > requirements.txt
   ```

---

## Step 2: Flask App Initialization

### `app/__init__.py`
```python
from flask import Flask
from dotenv import load_dotenv
import os

from app.models import db
from app.schemas import api
from app.routes import register_routes

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    api.init_app(app)

    # Register routes
    register_routes(api)

    return app
```

---

## Step 3: Define Database Models

### `app/models/__init__.py`
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

### `app/models/user.py`
```python
from app.models import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
```

### `app/models/post.py`
```python
from app.models import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.content[:20]}')"
```

---

## Step 4: Define API Schemas

### `app/schemas/__init__.py`
```python
from flask_restx import Api

api = Api(
    title="Flask-Migrate API",
    description="An API for managing users and posts, demonstrating database migrations and schema validation using Flask-Migrate and Flask-RESTx.",
    version="1.0"
)
```

### `app/schemas/user_schema.py`
```python
from flask_restx import fields
from app.schemas import api

user_model = api.model(
    "User",
    {
        "id": fields.Integer(readonly=True, description="Unique identifier of the user"),
        "username": fields.String(required=True, description="Username of the user"),
        "email": fields.String(required=True, description="Email of the user"),
    },
)
```

### `app/schemas/post_schema.py`
```python
from flask_restx import fields
from app.schemas import api

post_model = api.model(
    "Post",
    {
        "id": fields.Integer(readonly=True, description="Unique identifier of the post"),
        "title": fields.String(required=True, description="Title of the post"),
        "content": fields.String(required=True, description="Content of the post"),
        "user_id": fields.Integer(required=True, description="ID of the user who authored the post"),
    },
)
```

---

## Step 5: Define API Routes

### `app/routes/__init__.py`
```python
def register_routes(api):
    from app.routes.user_routes import user_ns
    from app.routes.post_routes import post_ns

    api.add_namespace(user_ns)
    api.add_namespace(post_ns)
```

### `app/routes/user_routes.py`
```python
from flask_restx import Namespace, Resource
from app.schemas import user_model

user_ns = Namespace("users", description="User operations")

@user_ns.route("/")
class UserList(Resource):
    @user_ns.marshal_with(user_model, as_list=True)
    def get(self):
        """List all users"""
        return [{"id": 1, "username": "johndoe", "email": "johndoe@example.com"}]

    @user_ns.expect(user_model)
    def post(self):
        """Create a user"""
        return {"message": "User created successfully"}, 201
```

### `app/routes/post_routes.py`
```python
from flask_restx import Namespace, Resource
from app.schemas import post_model

post_ns = Namespace("posts", description="Post operations")

@post_ns.route("/")
class PostList(Resource):
    @post_ns.marshal_with(post_model, as_list=True)
    def get(self):
        """List all posts"""
        return [
            {"id": 1, "title": "Post Title", "content": "Content of the post", "user_id": 1}
        ]

    @post_ns.expect(post_model)
    def post(self):
        """Create a post"""
        return {"message": "Post created successfully"}, 201
```

---

## Step 6: Run the Application

### `run.py`
```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

---

## Step 7: Set Up Environment Variables

### `.env`
```plaintext
DATABASE_URI="mysql+mysqlconnector://root:top!secret@localhost:3307/flask_migrate"
FLASK_APP=run.py
```

---

## Step 8: Initialize Database Migrations

1. Initialize migrations:
   ```bash
   flask db init
   ```

2. Create the first migration:
   ```bash
   flask db migrate -m "Initial migration"
   ```

3. Apply the migration:
   ```bash
   flask db upgrade
   ```

---

## Step 9: Running the Application

Start the Flask development server:
```bash
flask run
```

Access the API documentation at `http://127.0.0.1:5000/swagger`.

Let me know if you need further clarifications or additions!
