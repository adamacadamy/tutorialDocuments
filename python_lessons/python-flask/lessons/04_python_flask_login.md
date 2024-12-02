
# Guide to Flask-Login with MySQL

Flask-Login is an extension for handling user session management in Flask applications. It provides tools to manage user authentication and ensure that users are logged in to access specific views.

---

## **1. Setting Up Flask-Login**

### **Install Required Libraries**
Install Flask-Login and MySQL dependencies:
```bash
pip install flask-login flask-sqlalchemy pymysql
```

### **Project Structure**
```
flask_project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth.py  # Authentication routes
├── migrations/  # Created by Flask-Migrate
├── templates/  # HTML templates for the app
├── run.py
├── requirements.txt
```

---

## **2. Configure Flask-Login**

### **Database Setup in `__init__.py`**
```python
# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # MySQL Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/db_name"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "your_secret_key"  # Replace with a strong secret key

    db.init_app(app)
    login_manager.init_app(app)

    # Redirect unauthorized users to the login page
    login_manager.login_view = "auth.login"

    return app
```

Replace `username`, `password`, `localhost`, and `db_name` with your MySQL credentials.

---

## **3. Create User Model**

Define the `User` model in `models.py`. Flask-Login requires the implementation of specific methods to manage user authentication.

```python
# app/models.py
from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # Store hashed passwords

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
```

---

## **4. Initialize Flask-Login**

### **User Loader Callback**
Add the `user_loader` callback in `__init__.py`:
```python
# app/__init__.py
from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

This function tells Flask-Login how to retrieve a user object from the database.

---

## **5. Create Authentication Routes**

Create `auth.py` to handle login, logout, and registration.

```python
# app/auth.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app import db

auth = Blueprint("auth", __name__)

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

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
```

---

## **6. Protecting Routes**

In `routes.py`, protect routes with `@login_required`:

```python
# app/routes.py
from flask import render_template
from flask_login import login_required, current_user
from app import db

def register_routes(app):
    @app.route("/")
    @login_required
    def home():
        return render_template("home.html", user=current_user)
```

---

## **7. HTML Templates**

### **Login Page (`login.html`)**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <p>Email: <input type="email" name="email" required></p>
        <p>Password: <input type="password" name="password" required></p>
        <button type="submit">Login</button>
    </form>
    <p>Don't have an account? <a href="{{ url_for('auth.register') }}">Register here</a>.</p>
</body>
</html>
```

### **Registration Page (`register.html`)**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <p>Username: <input type="text" name="username" required></p>
        <p>Email: <input type="email" name="email" required></p>
        <p>Password: <input type="password" name="password" required></p>
        <button type="submit">Register</button>
    </form>
    <p>Already have an account? <a href="{{ url_for('auth.login') }}">Login here</a>.</p>
</body>
</html>
```

### **Home Page (`home.html`)**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome, {{ user.username }}!</h1>
    <a href="{{ url_for('auth.logout') }}">Logout</a>
</body>
</html>
```

---

## **8. Applying Database Migrations**

1. **Initialize Flask-Migrate**:
   ```bash
   flask db init
   ```

2. **Generate Migration Script**:
   ```bash
   flask db migrate -m "Add User model"
   ```

3. **Apply Migrations**:
   ```bash
   flask db upgrade
   ```

---

## **9. Testing the Application**

1. **Run the Flask App**:
   ```bash
   flask run
   ```

2. **Visit the App**:
   - **Register**: Go to `http://127.0.0.1:5000/register` to create a new account.
   - **Login**: Go to `http://127.0.0.1:5000/login` to log in.
   - **Access Protected Route**: After logging in, access the homepage at `http://127.0.0.1:5000`.

---

## **10. Summary**

- **Flask-Login** handles user session management, making it easy to implement user authentication.
- Passwords are securely stored using **Werkzeug’s hashing functions**.
- Use **@login_required** to restrict access to specific routes.
- Protect sensitive pages with proper redirections and logout functionality.
