# **Guide to Flask-Login with MySQL and Token-Based Authentication**

Flask-Login manages user sessions, while JSON Web Tokens (JWTs) are ideal for stateless, token-based authentication. This guide integrates both methods for flexibility.

---

## **1. Setting Up Flask-Login and JWT**

### **Install Required Libraries**
Install Flask-Login, Flask-JWT-Extended, and MySQL dependencies:
```bash
pip install flask-login flask-sqlalchemy pymysql flask-jwt-extended
```

### **Updated Project Structure**
```
flask_project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth.py  # Authentication routes (sessions & JWTs)
├── migrations/  # Created by Flask-Migrate
├── templates/  # HTML templates for the app
├── run.py
├── requirements.txt
```

---

## **2. Configure Flask-Login and JWT**

### **Update `__init__.py`**
Configure Flask-Login and Flask-JWT-Extended for session-based and token-based authentication:

```python
# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
login_manager = LoginManager()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # MySQL Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/db_name"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "your_secret_key"  # For Flask sessions
    app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"  # For JWTs

    db.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)

    # Redirect unauthorized users to the login page
    login_manager.login_view = "auth.login"

    return app
```

---

## **3. User Model**

Add methods to generate and validate JWTs in `User`:

```python
# app/models.py
from app import db
from flask_login import UserMixin
from flask_jwt_extended import create_access_token

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # Hashed password

    def get_jwt(self):
        return create_access_token(identity=self.id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
```

---

## **4. User Loader and JWT Callbacks**

### **Load User for Flask-Login**
```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

### **Optional JWT User Loading**
For JWT-based user access, you can create a function to retrieve user identity:
```python
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()
def current_user():
    user_id = get_jwt_identity()
    return User.query.get(user_id)
```

---

## **5. Authentication Routes**

Update `auth.py` to support **session-based login** and **token-based authentication**.

```python
# app/auth.py
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from flask_jwt_extended import jwt_required, create_access_token
from app.models import User
from app import db

auth = Blueprint("auth", __name__)

# Registration
@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"], method="sha256")

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")

# Session-based Login
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password.", "danger")

    return render_template("login.html")

# Token-based Login
@auth.route("/token", methods=["POST"])
def login_token():
    email = request.json.get("email")
    password = request.json.get("password")

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        token = user.get_jwt()
        return jsonify({"access_token": token}), 200
    else:
        return jsonify({"msg": "Invalid email or password"}), 401

# Logout (Session-based)
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
```

---

## **6. Protecting Routes**

### **Session-Based Protection**
Use `@login_required`:
```python
@app.route("/")
@login_required
def home():
    return render_template("home.html", user=current_user)
```

### **Token-Based Protection**
Use `@jwt_required`:
```python
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({"msg": f"Hello, {user.username}!"}), 200
```

---

## **7. Testing Token-Based Authentication**

Test the token endpoint and protected routes using tools like **Postman** or **curl**.

### **1. Obtain Token**
Send a POST request to `/token` with JSON data:
```json
{
  "email": "test@example.com",
  "password": "password123"
}
```

Response:
```json
{
  "access_token": "your_jwt_token"
}
```

### **2. Access Protected Route**
Send a GET request to `/protected` with the JWT in the `Authorization` header:
```
Authorization: Bearer your_jwt_token
```

Response:
```json
{
  "msg": "Hello, username!"
}
```

---

## **8. Updated Summary**

- **Session-Based Authentication**: Use Flask-Login for traditional user sessions.
- **Token-Based Authentication**: Use JWTs for stateless API access.
- **Password Security**: Store hashed passwords securely using **Werkzeug**.
- **Flexibility**: Combine session-based and token-based methods for hybrid applications.

This guide now supports modern API authentication using JWT while preserving traditional user session management.
