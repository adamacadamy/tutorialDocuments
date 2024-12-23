# **Guide to Flask-Login with MySQL and Token-Based Authentication**

Flask-Login manages user sessions, while JSON Web Tokens (JWTs) are ideal for stateless, token-based authentication. This guide integrates both methods for flexibility, following a structured project layout.

---

## **Project Structure**

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
├── templates/               # HTML templates for the app
│   ├── base.html            # Base HTML template
│   ├── register.html        # Registration page
│   └── login.html           # Login page
├── .env                     # Store database credentials and configuration
├── .venv/                   # Virtual environment (recommended for dependencies)
├── requirements.txt         # Python dependencies
└── run.py                   # Application entry point
```

---

## **Step 1: Application Setup**

### `run.py`
```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
```

---

## **Step 2: Initialize Flask App**

### `app/__init__.py`
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

# Extensions
db = SQLAlchemy()
login_manager = LoginManager()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # MySQL Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/db_name"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "your_secret_key"
    app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = "auth.login"

    # Register routes
    from app.routes import register_blueprints
    register_blueprints(app)

    return app
```

---

## **Step 3: Database Models**

### `app/models/__init__.py`
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

### `app/models/user.py`
```python
from app.models import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_jwt_extended import create_access_token

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def generate_jwt(self):
        return create_access_token(identity=self.id)

    @staticmethod
    def create_user(username, email, password):
        hashed_password = generate_password_hash(password)
        return User(username=username, email=email, password=hashed_password)
```

---

## **Step 4: Authentication Routes**

### `app/routes/__init__.py`
```python
def register_blueprints(app):
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
```

### `app/routes/auth.py`
```python
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from flask_jwt_extended import jwt_required, create_access_token
from app.models.user import db, User

auth_bp = Blueprint("auth", __name__)

# Registration
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])

        if User.query.filter_by(username=username).first():
            flash("Username already exists!", "danger")
        elif User.query.filter_by(email=email).first():
            flash("Email already exists!", "danger")
        else:
            user = User.create_user(username, email, password)
            db.session.add(user)
            db.session.commit()
            flash("Registration successful!", "success")
            return redirect(url_for("auth.login"))

    return render_template("register.html")

# Session-based Login
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("auth.dashboard"))
        else:
            flash("Invalid email or password.", "danger")

    return render_template("login.html")

# Token-based Login
@auth_bp.route("/token", methods=["POST"])
def login_token():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        token = user.generate_jwt()
        return jsonify({"access_token": token}), 200

    return jsonify({"msg": "Invalid email or password"}), 401

# Protected Resource
@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    return jsonify({"msg": f"Hello, {user.username}!"})

# Logout
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "info")
    return redirect(url_for("auth.login"))
```

---

## **Step 5: Templates**

### `templates/base.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Flask Authentication{% endblock %}</title>
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
    <div><label>Username</label><input name="username" required></div>
    <div><label>Email</label><input name="email" type="email" required></div>
    <div><label>Password</label><input name="password" type="password" required></div>
    <button type="submit">Register</button>
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
    <div><label>Email</label><input name="email" type="email" required></div>
    <div><label>Password</label><input name="password" type="password" required></div>
    <button type="submit">Login</button>
</form>
{% endblock %}
```

---

## **Step 6: Environment Configuration**

### `.env`
```
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
SQLALCHEMY_DATABASE_URI=mysql+pymysql://username:password@localhost/db_name
SQLALCHEMY_TRACK_MODIFICATIONS=False
```

---

## **Step 7: Requirements**

### `requirements.txt`
```
Flask
Flask-SQLAlchemy
Flask-Login
Flask-Migrate
Flask-JWT-Extended
Werkzeug
pymysql
```
