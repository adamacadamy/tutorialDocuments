
# Comprehensive Flask-SQLAlchemy Tutorial

This guide will walk you through setting up **Flask-SQLAlchemy** with **MySQL** and **PostgreSQL**, performing CRUD operations, applying query filters, and executing raw SQL queries. You'll also create a simple CRUD application.

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

## **5. CRUD Operations**

### **Insert Data**
```python
user = User(username="Alice", email="alice@example.com")
db.session.add(user)
db.session.commit()
```

### **Query Data**
```python
users = User.query.all()  # Get all users
user = User.query.filter_by(username="Alice").first()  # Filter by username
```

### **Update Data**
```python
user = User.query.filter_by(username="Alice").first()
user.email = "alice.new@example.com"
db.session.commit()
```

### **Delete Data**
```python
user = User.query.filter_by(username="Alice").first()
db.session.delete(user)
db.session.commit()
```

---

## **6. Advanced Query Filters**

### **Filter Posts by User**
```python
posts = Post.query.filter(Post.user_id == user.id).all()
```

### **Search Content for Keywords**
```python
posts = Post.query.filter(Post.content.like("%keyword%")).all()
```

### **Paginate Results**
```python
paginated_posts = Post.query.paginate(page=1, per_page=5)
```

---

## **7. Executing Raw SQL Queries**

### **Insert Data**
```python
db.session.execute(
    "INSERT INTO user (username, email) VALUES (:username, :email)",
    {"username": "Bob", "email": "bob@example.com"}
)
db.session.commit()
```

### **Fetch Data**
```python
result = db.session.execute("SELECT * FROM user WHERE username = :username", {"username": "Bob"})
for row in result:
    print(row)
```

### **Update Data**
```python
db.session.execute(
    "UPDATE user SET email = :email WHERE username = :username",
    {"username": "Bob", "email": "bob.new@example.com"}
)
db.session.commit()
```

### **Delete Data**
```python
db.session.execute("DELETE FROM user WHERE username = :username", {"username": "Bob"})
db.session.commit()
```

---

## **8. Building a CRUD Application**

### **Routes in `routes.py`**
```python
from flask import render_template, request, redirect, url_for, flash
from app import db
from app.models import User, Post

def register_routes(app):
    @app.route("/")
    def home():
        users = User.query.all()
        return render_template("home.html", users=users)

    @app.route("/user/add", methods=["GET", "POST"])
    def add_user():
        if request.method == "POST":
            username = request.form["username"]
            email = request.form["email"]
            new_user = User(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash(f"User {username} added!")
            return redirect(url_for("home"))
        return render_template("add_user.html")

    @app.route("/user/<int:user_id>/update", methods=["GET", "POST"])
    def update_user(user_id):
        user = User.query.get_or_404(user_id)
        if request.method == "POST":
            user.username = request.form["username"]
            user.email = request.form["email"]
            db.session.commit()
            flash(f"User {user.username} updated!")
            return redirect(url_for("home"))
        return render_template("update_user.html", user=user)

    @app.route("/user/<int:user_id>/delete", methods=["POST"])
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        flash(f"User {user.username} deleted!")
        return redirect(url_for("home"))
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

### **Summary**

- **Flask-SQLAlchemy** integrates easily with MySQL, PostgreSQL, or SQLite.
- CRUD operations and query filters simplify data management.
- Execute raw SQL queries when needed for advanced control.
- Build a full-featured CRUD application using Flask routes and templates.
