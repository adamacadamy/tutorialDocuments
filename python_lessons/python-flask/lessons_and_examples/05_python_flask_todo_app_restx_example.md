# Flask To-Do Management with Authentication and REST API

## Overview
This Flask-based **To-Do Management System** supports:
- **User authentication** (registration & login)
- **REST API endpoints** for managing to-do tasks
- **MySQL database integration** with SQLAlchemy ORM
- **Web forms for user interaction**
- **Migrations using Flask-Migrate**

---

## Project Structure
```
├── .gitignore               # Ignore unnecessary files
├── app/                     # Application logic
│   ├── __init__.py          # Initialize Flask app
│   ├── models/              # Database models
│   │   ├── __init__.py      # Initialize SQLAlchemy
│   │   ├── user.py          # User model
│   │   └── todo.py          # To-Do model
│   ├── routes/              # API routes
│   │   ├── __init__.py      # Initialize routes
│   │   ├── auth.py          # Authentication routes
│   │   ├── todo.py          # To-Do routes
│   │   ├── views.py         # Routes for rendering HTML templates
│   ├── schemas/             # API schemas
│   │   ├── __init__.py      # Initialize schemas
│   │   ├── user_schema.py   # User schema
│   │   └── todo_schema.py   # To-Do schema
│   ├── forms/               # Web forms
│   │   ├── __init__.py      # Initialize forms
│   │   ├── login_form.py    # Login form
│   │   ├── register_form.py # Registration form
│   │   └── todo_form.py     # To-Do form
│   ├── templates/           # HTML templates for web views
│       ├── base.html        # Base template
│       ├── login.html       # Login page
│       ├── register.html    # Registration page
│       ├── todo.html        # To-Do page
├── static/                  # Static files (CSS, JS, images)
│   ├── style.css            # Stylesheet
│   ├── script.js            # JavaScript file
├── migrations/              # Flask-Migrate folder
├── .env                     # Store database credentials and configuration
├── .venv/                   # Virtual environment
├── requirements.txt         # Python dependencies
└── run.py                   # Application entry point
```

---

## Step 0: Setting Up Virtual Environment

### **Create and Activate Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```


### `requirements.txt`
```
Flask
Flask-RESTx
Flask-SQLAlchemy
Flask-Migrate
Flask-WTF
python-dotenv
mysql-connector-python
Werkzeug
```

### **Install Dependencies**
```bash
pip install -r requirements.txt
```

## Step 1: Application Initialization

### `app/__init__.py`
```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from dotenv import load_dotenv
from .routes import register_routes
from .schemas import api
from .models import db

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)
    Migrate(app, db)
    api.init_app(app)
    register_routes(api)

    return app
```

---

## Step 2: Database Models

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
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    todos = db.relationship("ToDo", backref="user", lazy=True)

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
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
```

---

## Step 3: Web Forms

### `app/forms/login_form.py`
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
```

### `app/forms/register_form.py`
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")
```

### `app/forms/todo_form.py`
```python
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ToDoForm(FlaskForm):
    task = StringField("Task", validators=[DataRequired()])
    is_completed = BooleanField("Completed")
    submit = SubmitField("Add Task")
```

---
## Step 4: API Schemas

### `app/schemas/__init__.py`
```python
from flask_restx import Api

api = Api(
    title="To-Do Management API",
    version="1.0",
    description="API for managing user authentication and to-do items."
)
```

### `app/schemas/user_schema.py`
```python
from flask_restx import fields
from app.schemas import api

user_model = api.model(
    "User",
    {
        "id": fields.Integer(readonly=True, description="User ID"),
        "username": fields.String(required=True, description="Username"),
        "email": fields.String(required=True, description="Email"),
        "password": fields.String(required=True, description="Password"),
    }
)
```

### `app/schemas/todo_schema.py`
```python
from flask_restx import fields
from app.schemas import api

todo_model = api.model(
    "ToDo",
    {
        "id": fields.Integer(readonly=True, description="To-Do ID"),
        "task": fields.String(required=True, description="Task description"),
        "is_completed": fields.Boolean(description="Completion status"),
        "user_id": fields.Integer(description="User ID")
    }
)
```


## Step 5: Templates

### `app/templates/base.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}To-Do Management{% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <header>
        <h1>To-Do Management</h1>
        <nav>
            <a href="/login">Login</a> |
            <a href="/register">Register</a> |
            <a href="/todo">To-Do List</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <script src="/static/script.js"></script>
</body>
</html>
```

### `app/templates/login.html`
```html
{% extends "base.html" %}
{% block title %}Login{% endblock %}
{% block content %}
<h2>Login</h2>
<form method="POST">
    {{ form.hidden_tag() }}
    <div>{{ form.username.label }} {{ form.username }}</div>
    <div>{{ form.password.label }} {{ form.password }}</div>
    <div>{{ form.submit }}</div>
</form>
{% endblock %}
```

### `app/templates/register.html`
```html
{% extends "base.html" %}
{% block title %}Register{% endblock %}
{% block content %}
<h2>Register</h2>
<form method="POST">
    {{ form.hidden_tag() }}
    <div>{{ form.username.label }} {{ form.username }}</div>
    <div>{{ form.email.label }} {{ form.email }}</div>
    <div>{{ form.password.label }} {{ form.password }}</div>
    <div>{{ form.submit }}</div>
</form>
{% endblock %}
```

### `app/templates/todo.html`
```html
{% extends "base.html" %}
{% block title %}To-Do List{% endblock %}
{% block content %}
<h2>To-Do List</h2>
<form method="POST">
    {{ form.hidden_tag() }}
    <div>{{ form.task.label }} {{ form.task }}</div>
    <div>{{ form.is_completed.label }} {{ form.is_completed }}</div>
    <div>{{ form.submit }}</div>
</form>
{% endblock %}
```


## Step 6: Static Files

### `static/style.css`
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
}

header {
    background-color: #333;
    color: white;
    padding: 10px 20px;
    text-align: center;
}

header h1 {
    margin: 0;
    font-size: 24px;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 10px;
    font-size: 18px;
}

main {
    margin: 20px auto;
    max-width: 800px;
    padding: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

h2 {
    color: #333;
    font-size: 22px;
    margin-bottom: 20px;
}

form div {
    margin-bottom: 15px;
}

form input[type="submit"] {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
}

form input[type="submit"]:hover {
    background-color: #0056b3;
}
```

### `static/script.js`
```javascript
document.addEventListener("DOMContentLoaded", () => {
    console.log("JavaScript is working!");
});
```

## Step 7: Application Entry Point

### `run.py`
```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```


## Step 8: API Routes

### `app/routes/__init__.py`
```python
def register_routes(api):
    from app.routes.auth import auth_ns
    from app.routes.todo import todo_ns

    api.add_namespace(auth_ns, path="/auth")
    api.add_namespace(todo_ns, path="/todo")
```

### `app/routes/auth.py`
```python
from flask import request
from flask_restx import Namespace, Resource
from app.models.user import User
from app.models import db

auth_ns = Namespace("auth", description="Authentication management")

@auth_ns.route("/register")
class Register(Resource):
    def post(self):
        data = request.json
        username, email, password = data["username"], data["email"], data["password"]

        if User.query.filter_by(username=username).first():
            return {"message": "Username already exists"}, 400
        if User.query.filter_by(email=email).first():
            return {"message": "Email already exists"}, 400

        new_user = User.create_user(username, email, password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully"}, 201
```

### `app/routes/todo.py`
```python
from flask import request
from flask_restx import Namespace, Resource
from app.models.todo import ToDo
from app.models import db

todo_ns = Namespace("todo", description="To-Do management")

@todo_ns.route("/")
class ToDoList(Resource):
    def get(self):
        """Retrieve all to-do tasks."""
        return [todo.to_dict() for todo in ToDo.query.all()], 200

    def post(self):
        """Create a new to-do task."""
        data = request.json
        new_todo = ToDo(task=data["task"], is_completed=data.get("is_completed", False), user_id=data["user_id"])
        db.session.add(new_todo)
        db.session.commit()
        return {"message": "To-Do task created successfully."}, 201
```

## Step 9: Html views route
### `app/routes/views.py`
```python
from flask import Blueprint, render_template
from app.forms.login_form import LoginForm
from app.forms.register_form import RegisterForm
from app.forms.todo_form import ToDoForm

views_bp = Blueprint("views", __name__)

@views_bp.route("/login", methods=["GET"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@views_bp.route("/register", methods=["GET"])
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)

@views_bp.route("/todo", methods=["GET"])
def todo():
    form = ToDoForm()
    return render_template("todo.html", form=form)
```
## Step 10: Migrations and Configuration

### **Environment Variables**
`.env`
```
SECRET_KEY=your_secret_key
DATABASE_URI=mysql+mysqlconnector://root:top!secreat@localhost:3307/todo_db
```

### **Migration Commands**
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
