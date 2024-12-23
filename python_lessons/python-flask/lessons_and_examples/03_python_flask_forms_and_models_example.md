# Flask Example: Forms with Models

## Overview
This example demonstrates how to use Flask-WTF forms for handling user input and integrate it with SQLAlchemy models for data storage. The application includes:
- Flask-WTF for form handling
- SQLAlchemy models for database interactions
- Web-based user registration and login forms

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
│   └── routes/              # Folder for application routes
│       ├── __init__.py      # Initialize routes
│       ├── auth.py          # Authentication routes
├── migrations/              # Flask-Migrate folder
├── .env                     # Store database credentials and configuration
├── .venv/                   # Virtual environment (recommended for dependencies)
├── requirements.txt         # Python dependencies
└── run.py                   # Application entry point
```

---

## Step 1: Application Setup

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
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:password@localhost/flask_forms"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "your_secret_key"

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import register_blueprints
    register_blueprints(app)

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

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def create_user(username, email, password):
        hashed_password = generate_password_hash(password)
        return User(username=username, email=email, password_hash=hashed_password)
```

---

## Step 4: Forms

### `app/forms.py`
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
```

---

## Step 5: Authentication Routes

### `app/routes/__init__.py`
```python
def register_blueprints(app):
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
```

### `app/routes/auth.py`
```python
from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import RegistrationForm, LoginForm
from app.models.user import db, User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        if User.query.filter_by(username=username).first():
            flash("Username already exists!", "danger")
        elif User.query.filter_by(email=email).first():
            flash("Email already exists!", "danger")
        else:
            new_user = User.create_user(username, email, password)
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            flash("Login successful!", "success")
            return redirect(url_for("auth.dashboard"))
        else:
            flash("Invalid email or password!", "danger")

    return render_template("login.html", form=form)

@auth_bp.route("/dashboard")
def dashboard():
    return "Welcome to your dashboard!"
```

---

## Step 6: Templates

### `templates/base.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Flask Forms{% endblock %}</title>
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

### `templates/register.html`
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
    <div>{{ form.confirm_password.label }} {{ form.confirm_password }}</div>
    <div>{{ form.submit }}</div>
</form>
{% endblock %}
```

### `templates/login.html`
```html
{% extends "base.html" %}
{% block title %}Login{% endblock %}
{% block content %}
<h2>Login</h2>
<form method="POST">
    {{ form.hidden_tag() }}
    <div>{{ form.email.label }} {{ form.email }}</div>
    <div>{{ form.password.label }} {{ form.password }}</div>
    <div>{{ form.submit }}</div>
</form>
{% endblock %}
```

---

## Step 7: Environment Configuration

### `.env`
```
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://root:password@localhost/flask_forms
SQLALCHEMY_TRACK_MODIFICATIONS=False
```

---

## Step 8: Requirements

### `requirements.txt`
```
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-WTF
mysql-connector-python
Werkzeug
```
