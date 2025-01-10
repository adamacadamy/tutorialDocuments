# Flask REST API for Library Management System

## Project Overview
This project is a **RESTful API** built with Flask for managing books, authors, and borrowers in a library system. It includes:
- **CRUD operations** for Books, Authors, and Borrowers.
- **Swagger documentation** using Flask-RESTx.
- **SQLAlchemy** for ORM and database management.
- **Flask-Migrate** for handling schema migrations.
- **Environment variable support** with `python-dotenv`.

### API Overview

#### API Endpoints

##### 1. Books
- **`GET /books/`**: List all books.
- **`POST /books/`**: Add a new book.
- **`GET /books/<id>`**: Retrieve a book by ID.
- **`DELETE /books/<id>`**: Remove a book by ID.

##### 2. Authors
- **`GET /authors/`**: List all authors.
- **`POST /authors/`**: Add a new author.
- **`GET /authors/<id>`**: Retrieve an author by ID.

##### 3. Borrowers
- **`GET /borrowers/`**: List all borrowers.
- **`POST /borrowers/`**: Register a new borrower.
- **`POST /borrowers/<id>/borrow`**: Borrow a book.

---

#### API Models

##### 1. Book Model
- **`id`** *(Integer)*: Unique identifier of the book (read-only).
- **`title`** *(String)*: Title of the book (required).
- **`author_id`** *(Integer)*: ID of the associated author (required).
- **`is_borrowed`** *(Boolean)*: Status of whether the book is borrowed.

##### 2. Author Model
- **`id`** *(Integer)*: Unique identifier of the author (read-only).
- **`name`** *(String)*: Name of the author (required).

##### 3. Borrower Model
- **`id`** *(Integer)*: Unique identifier of the borrower (read-only).
- **`name`** *(String)*: Name of the borrower (required).
- **`borrowed_books`** *(String)*: Comma-separated list of borrowed book IDs.

---

## Project Structure
```plaintext
pythonFlaskLibrary/
├── app/                   # Main app directory
│   ├── __init__.py        # Main app file with configurations
│   ├── models/            # Directory for database models
│   │   ├── __init__.py    # SQLAlchemy setup and model imports
│   │   ├── book.py        # Database model for Book
│   │   ├── author.py      # Database model for Author
│   │   └── borrower.py    # Database model for Borrower
│   ├── schemas/           # Directory for Flask-RESTx schemas
│   │   ├── __init__.py    # Initialize schemas
│   │   ├── book_schema.py # Schema for Book
│   │   ├── author_schema.py # Schema for Author
│   │   └── borrower_schema.py # Schema for Borrower
│   ├── routes/            # Directory for API routes
│   │   ├── __init__.py    # Register routes function
│   │   ├── books.py       # Routes for Book API
│   │   ├── authors.py     # Routes for Author API
│   │   └── borrowers.py   # Routes for Borrower API
│   ├── templates/         # Web views for interacting with the API
│       ├── base.html
│       ├── books.html
│       ├── authors.html
│       └── borrowers.html
├── static/                # Static files (CSS, JS, images)
│   ├── style.css
│   ├── script.js
├── migrations/            # Database migrations (created by Flask-Migrate)
├── .env                   # Environment variables
├── .venv/                 # Virtual environment directory
├── run.py                 # Entry point for running the application
└── requirements.txt       # Python dependencies
```

---

## Step-by-Step Implementation

### 1. Environment Setup

#### Install Dependencies

1. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install the dependencies:
   ```bash
   pip install flask flask-restx flask-sqlalchemy flask-migrate python-dotenv mysql-connector-python
   ```

3. Save dependencies to `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

---

### 2. Initialize the Flask App

#### `app/__init__.py`
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

### 3. Database Models

#### `app/models/__init__.py`
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

#### `app/models/book.py`
```python
from app.models import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.relationship('Author', back_populates='books')
    is_borrowed = db.Column(db.Boolean, default=False)
```

#### `app/models/author.py`
```python
from app.models import db

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', back_populates='author')
```

#### `app/models/borrower.py`
```python
from app.models import db

class Borrower(db.Model):
    __tablename__ = 'borrowers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    borrowed_books = db.Column(db.Text)  # Comma-separated book IDs
```

---

### 4. API Schemas

#### `app/schemas/__init__.py`
```python
from flask_restx import Api

api = Api(
    title="Library Management System API",
    version="1.0",
    description="API for managing books, authors, and borrowers."
)
```

#### `app/schemas/book_schema.py`
```python
from flask_restx import fields
from app.schemas import api

book_model = api.model('Book', {
    'id': fields.Integer(readOnly=True, description='Unique identifier of the book'),
    'title': fields.String(required=True, description='Title of the book'),
    'author_id': fields.Integer(required=True, description='ID of the author'),
    'is_borrowed': fields.Boolean(description='Borrowed status of the book')
})
```

#### `app/schemas/author_schema.py`
```python
from flask_restx import fields
from app.schemas import api

author_model = api.model('Author', {
    'id': fields.Integer(readOnly=True, description='Unique identifier of the author'),
    'name': fields.String(required=True, description='Name of the author')
})
```

#### `app/schemas/borrower_schema.py`
```python
from flask_restx import fields
from app.schemas import api

borrower_model = api.model('Borrower', {
    'id': fields.Integer(readOnly=True, description='Unique identifier of the borrower'),
    'name': fields.String(required=True, description='Name of the borrower'),
    'borrowed_books': fields.String(description='Comma-separated list of borrowed book IDs')
})
```

---

### 5. API Routes

#### `app/routes/__init__.py`
```python
def register_routes(api):
    from app.routes.books import book_ns
    from app.routes.authors import author_ns
    from app.routes.borrowers import borrower_ns

    api.add_namespace(book_ns)
    api.add_namespace(author_ns)
    api.add_namespace(borrower_ns)
```

#### `app/routes/books.py`
```python
from flask_restx import Namespace, Resource
from app.models.book import Book
from app.models import db
from app.schemas.book_schema import book_model

book_ns = Namespace('books', description="Book operations")

@book_ns.route('/')
class BookList(Resource):
    @book_ns.marshal_list_with(book_model)
    def get(self):
        """List all books"""
        return Book.query.all()

    @book_ns.expect(book_model)
    def post(self):
        """Add a new book"""
        data = book_ns.payload
        new_book = Book(title=data['title'], author_id=data['author_id'])
        db.session.add(new_book)
        db.session.commit()
        return new_book, 201
```

---

### 6. Run the Application

#### `run.py`
```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

---

### 7. Set Up Environment Variables

#### `.env`
```plaintext
DATABASE_URI="mysql+mysqlconnector://root:top!secret@localhost:3307/library"
FLASK_APP=run.py
```

---

### 8. Web Templates

#### `app/templates/base.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Library Management{% endblock %}</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <header>
        <h1>Library Management System</h1>
        <nav>
            <a href="/books">Books</a> | 
            <a href="/authors">Authors</a> | 
            <a href="/borrowers">Borrowers</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2024 Library Management System</p>
    </footer>
</body>
</html>
```

#### `app/templates/books.html`
```html
{% extends "base.html" %}
{% block title %}Books{% endblock %}
{% block content %}
<h2>Books</h2>
<ul>
    {% for book in books %}
        <li>{{ book.title }} by {{ book.author.name }}{% if book.is_borrowed %} (Borrowed){% endif %}</li>
    {% endfor %}
</ul>
{% endblock %}
```

#### `app/templates/authors.html`
```html
{% extends "base.html" %}
{% block title %}Authors{% endblock %}
{% block content %}
<h2>Authors</h2>
<ul>
    {% for author in authors %}
        <li>{{ author.name }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

#### `app/templates/borrowers.html`
```html
{% extends "base.html" %}
{% block title %}Borrowers{% endblock %}
{% block content %}
<h2>Borrowers</h2>
<ul>
    {% for borrower in borrowers %}
        <li>{{ borrower.name }} (Books: {{ borrower.borrowed_books }})</li>
    {% endfor %}
</ul>
{% endblock %}
```

---

### 9. Static Files

#### `static/style.css`
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: white;
    padding: 1rem;
    text-align: center;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 1rem;
}

main {
    padding: 2rem;
}

footer {
    text-align: center;
    padding: 1rem;
    background-color: #333;
    color: white;
    margin-top: 2rem;
}
```

#### `static/script.js`
```javascript
console.log("Library Management System Loaded!");
```

---

### 10. Running the Application

1. Initialize the database migrations:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

2. Run the application:
   ```bash
   flask run
   ```

3. Access the API at `http://127.0.0.1:5000/` and the Swagger documentation at `http://127.0.0.1:5000/swagger`.

