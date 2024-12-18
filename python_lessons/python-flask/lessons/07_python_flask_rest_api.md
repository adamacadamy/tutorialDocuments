
# Comprehensive Flask REST API Tutorial

This guide covers setting up a Flask REST API with CRUD operations, database integration using SQLAlchemy, and additional features like error handling and request validation.

---

## **1. Setting Up Flask REST API**

### **Install Required Libraries**
Install Flask and other necessary libraries:
```bash
pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy
```

### **Project Structure**
```
flask_rest_api/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
├── migrations/  # Created by Flask-Migrate (optional)
├── run.py
├── requirements.txt
```

---

## **2. Configuring Flask**

### **Database and App Initialization in `__init__.py`**
```python
# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Database Configuration (MySQL Example)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/db_name"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    return app
```

---

## **3. Creating Models**

Define database models in `models.py`:
```python
# app/models.py
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', {self.age})"
```

---

## **4. Data Serialization**

### **Define Marshmallow Schemas in `schemas.py`**
```python
# app/schemas.py
from app.models import User
from app import db
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        sqla_session = db.session

    id = auto_field()
    name = auto_field()
    email = auto_field()
    age = auto_field()
```

---

## **5. Creating RESTful Routes**

### **Define Routes in `routes.py`**
```python
# app/routes.py
from flask import Blueprint, jsonify, request, abort
from app.models import User
from app.schemas import UserSchema
from app import db

api = Blueprint("api", __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Get All Users
@api.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)

# Get User by ID
@api.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return user_schema.jsonify(user)

# Create a New User
@api.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    name = data.get("name")
    email = data.get("email")
    age = data.get("age")

    if not name or not email or not age:
        return jsonify({"error": "Missing fields"}), 400

    new_user = User(name=name, email=email, age=age)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user), 201

# Update an Existing User
@api.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    user.age = data.get("age", user.age)

    db.session.commit()
    return user_schema.jsonify(user)

# Delete a User
@api.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200
```

---

## **6. Registering the Blueprint**

Update `run.py` to register the API blueprint:
```python
# run.py
from app import create_app
from app.routes import api

app = create_app()
app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
```

---

## **7. Testing the API**

### **Run the Flask App**
```bash
flask run
```

### **Endpoints Overview**
1. **Get All Users**:
   - **Endpoint**: `GET /api/users`
   - **Response**:
     ```json
     [
         {
             "id": 1,
             "name": "Alice",
             "email": "alice@example.com",
             "age": 30
         }
     ]
     ```

2. **Get User by ID**:
   - **Endpoint**: `GET /api/users/<id>`
   - **Response**:
     ```json
     {
         "id": 1,
         "name": "Alice",
         "email": "alice@example.com",
         "age": 30
     }
     ```

3. **Create a New User**:
   - **Endpoint**: `POST /api/users`
   - **Request Body**:
     ```json
     {
         "name": "Alice",
         "email": "alice@example.com",
         "age": 30
     }
     ```
   - **Response**:
     ```json
     {
         "id": 1,
         "name": "Alice",
         "email": "alice@example.com",
         "age": 30
     }
     ```

4. **Update a User**:
   - **Endpoint**: `PUT /api/users/<id>`
   - **Request Body**:
     ```json
     {
         "name": "Alice Johnson",
         "email": "alice.johnson@example.com"
     }
     ```
   - **Response**:
     ```json
     {
         "id": 1,
         "name": "Alice Johnson",
         "email": "alice.johnson@example.com",
         "age": 30
     }
     ```

5. **Delete a User**:
   - **Endpoint**: `DELETE /api/users/<id>`
   - **Response**:
     ```json
     {
         "message": "User deleted successfully"
     }
     ```

---

## **8. Enhancing the API**

### **Error Handling**
Add error handling for 404 and 500 errors:
```python
# run.py
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500
```

### **Pagination**
Modify the `GET /users` route to include pagination:
```python
# app/routes.py
@api.route("/users", methods=["GET"])
def get_users():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    users = User.query.paginate(page=page, per_page=per_page)
    return users_schema.jsonify(users.items)
```

---

## **9. Summary**

- **Flask-SQLAlchemy** is used for database integration.
- **Marshmallow** handles serialization/deserialization.
- Blueprint organization keeps the code modular.
- REST API includes CRUD operations with proper error handling and request validation.
