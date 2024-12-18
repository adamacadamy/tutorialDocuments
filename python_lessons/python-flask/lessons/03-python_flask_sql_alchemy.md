# Comprehensive Flask-SQLAlchemy Tutorial (Updated with Class-Based Routes)

This guide walks you through setting up **Flask-SQLAlchemy** with **MySQL** and **PostgreSQL**, performing CRUD operations, applying query filters, executing raw SQL queries, and using class-based routes for a cleaner structure.

---

## **1. Setting Up Flask-SQLAlchemy**

### **Install Required Libraries**
For **MySQL**:
```bash
pip install flask-sqlalchemy pymysql
```

For **PostgreSQL**:
```bash
pip install flask-sqlalchemy psycopg2-binary
```

### **Project Structure**
Organize your project:
```
flask_project/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
├── run.py
├── requirements.txt
```

---

## **2. Configuring the Database**

### **Database URI in `__init__.py`**

1. **For MySQL**:
   ```python
   app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/db_name"
   ```

2. **For PostgreSQL**:
   ```python
   app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://username:password@localhost/db_name"
   ```

Replace `username`, `password`, `localhost`, and `db_name` with your database credentials.

### **Initialize Flask-SQLAlchemy**
```python
# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"  # Default to SQLite
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    return app
```

---

## **3. Creating Models**

Define your models in `models.py`:
```python
# app/models.py
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.content[:20]}...')"
```

---

## **4. Creating the Database**

### **Run Database Initialization**
In `run.py`, create the database tables:
```python
# run.py
from app import create_app, db
from app.models import User, Post

app = create_app()

with app.app_context():
    db.create_all()  # Create tables

if __name__ == "__main__":
    app.run(debug=True)
```

Run the application:
```bash
python run.py
```
A `site.db` SQLite file will be created.

---

## **5. CRUD Operations with Class-Based Routes**

### **Routes in `routes.py`**
```python
from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from app import db
from app.models import User

class HomeView(MethodView):
    def get(self):
        users = User.query.all()
        return render_template("home.html", users=users)

class AddUserView(MethodView):
    def get(self):
        return render_template("add_user.html")

    def post(self):
        username = request.form["username"]
        email = request.form["email"]
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash(f"User {username} added!")
        return redirect(url_for("home"))

class UpdateUserView(MethodView):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return render_template("update_user.html", user=user)

    def post(self, user_id):
        user = User.query.get_or_404(user_id)
        user.username = request.form["username"]
        user.email = request.form["email"]
        db.session.commit()
        flash(f"User {user.username} updated!")
        return redirect(url_for("home"))

class DeleteUserView(MethodView):
    def post(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        flash(f"User {user.username} deleted!")
        return redirect(url_for("home"))

def register_routes(app):
    app.add_url_rule("/", view_func=HomeView.as_view("home"))
    app.add_url_rule("/user/add", view_func=AddUserView.as_view("add_user"), methods=["GET", "POST"])
    app.add_url_rule("/user/<int:user_id>/update", view_func=UpdateUserView.as_view("update_user"), methods=["GET", "POST"])
    app.add_url_rule("/user/<int:user_id>/delete", view_func=DeleteUserView.as_view("delete_user"), methods=["POST"])
```

---

### **Templates**

1. **`home.html`**:
   ```html
   <h1>All Users</h1>
   <ul>
   {% for user in users %}
       <li>{{ user.username }} ({{ user.email }}) 
           <a href="{{ url_for('update_user', user_id=user.id) }}">Update</a>
           <form action="{{ url_for('delete_user', user_id=user.id) }}" method="POST" style="display:inline;">
               <button type="submit">Delete</button>
           </form>
       </li>
   {% endfor %}
   </ul>
   <a href="{{ url_for('add_user') }}">Add User</a>
   ```

2. **`add_user.html`**:
   ```html
   <h1>Add User</h1>
   <form method="POST">
       <p>Username: <input type="text" name="username" required></p>
       <p>Email: <input type="email" name="email" required></p>
       <button type="submit">Add</button>
   </form>
   ```

3. **`update_user.html`**:
   ```html
   <h1>Update User</h1>
   <form method="POST">
       <p>Username: <input type="text" name="username" value="{{ user.username }}" required></p>
       <p>Email: <input type="email" name="email" value="{{ user.email }}" required></p>
       <button type="submit">Update</button>
   </form>
   ```

---

## **6. Advanced Query Filters**

You can still use advanced query filters or raw SQL queries if needed. These methods can be integrated into the class-based views as required.

---

This updated tutorial ensures your project structure is cleaner and more modular by leveraging class-based views. Let me know if you need further assistance!
