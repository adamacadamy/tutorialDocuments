# Flask Authentication with Flask-RESTx and Namespace

## Overview
This lesson demonstrates how to build a Flask application with authentication using Flask-RESTx and namespaces. The app includes both REST API endpoints and web-based user authentication.

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
from flask_restx import Api
from flask_migrate import Migrate
from app.models import db
from app.routes import initialize_routes

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:password@localhost/flask_auth"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "your_secret_key"

    db.init_app(app)
    migrate = Migrate(app, db)

    api = Api(app, version="1.0", title="Auth API", description="Authentication API using Flask-RESTx")
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

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def create_user(username, email, password):
        hashed_password = generate_password_hash(password)
        return User(username=username, email=email, password_hash=hashed_password)
```

---

## Step 4: Authentication Routes

### `app/routes/__init__.py`
```python
def initialize_routes(api):
    from app.routes.auth import auth_ns
    api.add_namespace(auth_ns)
```

### `app/routes/auth.py`
```python
from flask import request
from flask_restx import Namespace, Resource, fields
from app.models.user import User
from app.models import db

auth_ns = Namespace("auth", description="Authentication operations")

user_model = auth_ns.model("User", {
    "id": fields.Integer(readonly=True, description="The user unique identifier"),
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
    @auth_ns.expect(user_model, validate=True)
    @auth_ns.marshal_with(user_model, code=201)
    def post(self):
        data = request.json
        username = data["username"]
        email = data["email"]
        password = data["password"]

        if User.query.filter_by(username=username).first():
            auth_ns.abort(400, "Username already exists")
        if User.query.filter_by(email=email).first():
            auth_ns.abort(400, "Email already exists")

        new_user = User.create_user(username, email, password)
        db.session.add(new_user)
        db.session.commit()

        return new_user, 201

@auth_ns.route("/login")
class Login(Resource):
    @auth_ns.expect(login_model, validate=True)
    def post(self):
        data = request.json
        username = data["username"]
        password = data["password"]

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            auth_ns.abort(401, "Invalid username or password")

        return {"message": f"Welcome, {username}"}, 200
```

---

## Step 5: Environment Configuration

### `.env`
```
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://root:password@localhost/flask_auth
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
   ```
