# Flask Example Application: To-Do Management with Authentication

## Overview
This example demonstrates how to build a Flask application with:
- User authentication
- REST API endpoints
- Web-based To-Do management
- MySQL database integration

---

## Project Structure

The application follows this structure:

```
├── .gitignore               # Ignore unnecessary files
├── app/                     # Application logic
│   ├── __init__.py          # Initialize Flask app
│   ├── models/              # Folder for database models
│   │   ├── __init__.py      # Initialize SQLAlchemy
│   │   ├── user.py          # User model
│   │   └── todo.py          # To-Do model
│   └── routes/              # Folder for application routes
│       ├── __init__.py      # Initialize routes
│       ├── auth.py          # Authentication routes
│       └── todo.py          # To-Do routes
├── migrations/              # Flask-Migrate folder
├── .env                     # Store database credentials and configuration
├── .venv/                   # Virtual environment (recommended for dependencies)
├── requirements.txt         # Python dependencies
└── run.py                   # Application entry point
```

---

## Step 1: Application Setup
### Install Dependencies

####  Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

#### Install the dependencies:
   ```bash
   pip install flask flask-restx flask-sqlalchemy flask-migrate python-dotenv mysql-connector-python
   ```

#### Save dependencies to `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```
   
### `run.py`
```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
```

---

## Step 2: Initialize Flask App

### `app/__init__.py`
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_migrate import Migrate
from app.models import db
from app.routes import initialize_routes

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:password@localhost/flask_todo"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "your_secret_key"

    db.init_app(app)
    migrate = Migrate(app, db)

    api = Api(app, version="1.0", title="To-Do API", description="To-Do management API with authentication")
    initialize_routes(api)

    return app
```

---

## Step 3: Database Models

### `app/models/__init__.py`
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

### `app/models/user.py`
```python
from app.models import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    todos = db.relationship('ToDo', backref='user', lazy=True)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def create_user(username, email, password):
        hashed_password = generate_password_hash(password)
        return User(username=username, email=email, password_hash=hashed_password)
```

### `app/models/todo.py`
```python
from app.models import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```

---

## Step 4: Authentication and To-Do Routes

### `app/routes/__init__.py`
```python
def initialize_routes(api):
    from app.routes.auth import auth_ns
    from app.routes.todo import todo_ns
    api.add_namespace(auth_ns)
    api.add_namespace(todo_ns)
```

### `app/routes/auth.py`
```python
from flask import request
from flask_restx import Namespace, Resource, fields
from app.models.user import User
from app.models import db

auth_ns = Namespace("auth", description="Authentication operations")

user_model = auth_ns.model("User", {
    "username": fields.String(required=True, description="The user username"),
    "email": fields.String(required=True, description="The user email"),
    "password": fields.String(required=True, description="The user password")
})

login_model = auth_ns.model("Login", {
    "username": fields.String(required=True, description="The user username"),
    "password": fields.String(required=True, description="The user password")
})

@auth_ns.route("/register")
class Register(Resource):
    @auth_ns.expect(user_model)
    def post(self):
        data = request.json
        username = data["username"]
        email = data["email"]
        password = data["password"]

        if User.query.filter_by(username=username).first():
            return {"message": "Username already exists"}, 400
        if User.query.filter_by(email=email).first():
            return {"message": "Email already exists"}, 400

        new_user = User.create_user(username, email, password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully"}, 201

@auth_ns.route("/login")
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        data = request.json
        username = data["username"]
        password = data["password"]

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return {"message": "Invalid username or password"}, 401

        return {"message": f"Welcome, {username}"}, 200
```

### `app/routes/todo.py`
```python
from flask import request
from flask_restx import Namespace, Resource, fields
from app.models.todo import ToDo
from app.models import db

todo_ns = Namespace("todo", description="To-Do management operations")

todo_model = todo_ns.model("ToDo", {
    "task": fields.String(required=True, description="The to-do task"),
    "is_completed": fields.Boolean(description="Completion status")
})

@todo_ns.route("/")
class ToDoList(Resource):
    @todo_ns.marshal_list_with(todo_model)
    def get(self):
        return ToDo.query.all()

    @todo_ns.expect(todo_model)
    def post(self):
        data = request.json
        task = data["task"]
        is_completed = data.get("is_completed", False)

        new_todo = ToDo(task=task, is_completed=is_completed, user_id=1)  # Hardcoded user ID for simplicity
        db.session.add(new_todo)
        db.session.commit()

        return {"message": "To-Do created successfully"}, 201

@todo_ns.route("/<int:id>")
class ToDoItem(Resource):
    def delete(self, id):
        todo = ToDo.query.get_or_404(id)
        db.session.delete(todo)
        db.session.commit()
        return {"message": "To-Do deleted successfully"}, 200
```

---

## Step 5: Environment Configuration

### `.env`
```
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://root:password@localhost/flask_todo
SQLALCHEMY_TRACK_MODIFICATIONS=False
```

---

## Step 6: Requirements

### `requirements.txt`
```
Flask
Flask-RESTx
Flask-SQLAlchemy
Flask-Migrate
mysql-connector-python
Werkzeug
```

---

## Step 7: Migration Commands

1. Initialize the migration folder:
   ```bash
   flask db init
   ```

2. Generate the initial migration script:
   ```bash
   flask db migrate -m "Initial migration"
   ```

3. Apply the migrations to the database:
   ```bash
   flask db upgrade
   
