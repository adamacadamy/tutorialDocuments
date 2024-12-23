
# Guide to Flask-Migrate with MySQL

Flask-Migrate is an extension that uses Alembic for handling database migrations in Flask applications. It allows you to create and apply database schema changes without manually altering the database.

---

## **1. Setting Up Flask-Migrate**

### **Install Required Libraries**
Install Flask-Migrate and MySQL dependencies:
```bash
pip install flask-migrate pymysql
```

### **Project Structure**
```
flask_project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
├── migrations/  # Automatically created by Flask-Migrate
├── run.py
├── requirements.txt
```

---

## **2. Configure Flask-Migrate**

### **Database and Migrate Setup in `__init__.py`**
1. Configure Flask-SQLAlchemy and Flask-Migrate:
   ```python
   # app/__init__.py
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy
   from flask_migrate import Migrate

   db = SQLAlchemy()
   migrate = Migrate()

   def create_app():
       app = Flask(__name__)

       # MySQL Configuration
       app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/db_name"
       app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

       db.init_app(app)
       migrate.init_app(app, db)

       return app
   ```

Replace `username`, `password`, `localhost`, and `db_name` with your MySQL database credentials.

2. Add your models in `models.py`:
   ```python
   # app/models.py
   from app import db

   class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(80), unique=True, nullable=False)
       email = db.Column(db.String(120), unique=True, nullable=False)

       def __repr__(self):
           return f"User('{self.username}', '{self.email}')"
   ```

---

## **3. Initialize Flask-Migrate**

### **Step 1: Update `run.py`**
```python
# run.py
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

### **Step 2: Initialize Migrations**
Run the following commands to initialize Flask-Migrate:

1. **Activate the virtual environment (if not already activated)**:
   ```bash
   source flask_env/bin/activate  # On Linux/Mac
   flask_env\Scripts\activate    # On Windows
   ```

2. **Set Flask App Environment Variable**:
   ```bash
   export FLASK_APP=run.py  # On Linux/Mac
   set FLASK_APP=run.py     # On Windows
   ```

3. **Initialize the Migrations Directory**:
   ```bash
   flask db init
   ```

This will create a `migrations/` folder in your project.

---

## **4. Create and Apply Migrations**

### **Step 1: Generate the Migration Script**
After making changes to your models, generate a migration script:
```bash
flask db migrate -m "Initial migration"
```

This will create a migration script in the `migrations/versions/` directory.

### **Step 2: Apply the Migration**
Apply the migration to the MySQL database:
```bash
flask db upgrade
```

---

## **5. Adding a New Model**

If you need to add a new model or modify an existing one, follow these steps:

1. **Update `models.py`**:
   ```python
   class Post(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       title = db.Column(db.String(100), nullable=False)
       content = db.Column(db.Text, nullable=False)
       user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   ```

2. **Generate a New Migration**:
   ```bash
   flask db migrate -m "Add Post model"
   ```

3. **Apply the Migration**:
   ```bash
   flask db upgrade
   ```

---

## **6. Verifying Database Changes**

1. **Log in to MySQL**:
   ```bash
   mysql -u username -p
   ```

2. **Select the Database**:
   ```sql
   USE db_name;
   ```

3. **Check Tables**:
   ```sql
   SHOW TABLES;
   ```

4. **Inspect Columns in a Table**:
   ```sql
   DESCRIBE user;
   ```

---

## **Summary**

- **Flask-Migrate** simplifies database migrations using Alembic.
- You can create, modify, and upgrade your database schema without manually altering it.
- Combined with **Flask-SQLAlchemy**, it provides a powerful tool for managing database integrations.

Let me know if you’d like further help!
