# Flask REST API for Product and Category Management

## Project Overview
This project is a **RESTful API** built with Flask for managing products and their associated categories. It includes:
- **CRUD operations** for Products and Categories.
- **Swagger documentation** using Flask-RESTx.
- **SQLAlchemy** for ORM and database management.
- **Flask-Migrate** for handling schema migrations.
- **Environment variable support** with `python-dotenv`.

### API Overview

#### API Endpoints

##### 1. Products
- **`GET /products/`**: List all products.
- **`POST /products/`**: Create a new product.
- **`GET /products/<id>`**: Retrieve a product by ID.
- **`DELETE /products/<id>`**: Delete a product by ID.

##### 2. Categories
- **`GET /categories/`**: List all categories.
- **`POST /categories/`**: Create a new category.
- **`GET /categories/<id>`**: Retrieve a category by ID.
- **`DELETE /categories/<id>`**: Delete a category by ID.

---

#### API Models

##### 1. Product Model
- **`id`** *(Integer)*: Unique identifier of the product (read-only).
- **`name`** *(String)*: Name of the product (required).
- **`price`** *(Float)*: Price of the product (required).
- **`category`** *(Nested Category)*: The category associated with the product.

##### 2. Category Model
- **`id`** *(Integer)*: Unique identifier of the category (read-only).
- **`name`** *(String)*: Name of the category (required).
- **`description`** *(String)*: A brief description of the category.

---

## Project Structure
```plaintext
pythonFlaskProductCategory/
├── app/                   # Main app directory
│   ├── __init__.py        # Main app file with configurations
│   ├── models/            # Directory for database models
│   │   ├── __init__.py    # SQLAlchemy setup and model imports
│   │   ├── product.py     # Database model for Product
│   │   └── category.py    # Database model for Category
│   ├── schemas/           # Directory for Flask-RESTx schemas
│   │   ├── __init__.py    # Initialize schemas
│   │   ├── product_schema.py  # Schema for Product
│   │   └── category_schema.py # Schema for Category
│   ├── routes/            # Directory for API routes
│   │   ├── __init__.py    # Register routes function
│   │   ├── products.py    # Routes for Product API
│   │   └── categories.py  # Routes for Category API
│   ├── templates/         # Web views for interacting with the API
│       ├── base.html
│       ├── products.html
│       └── categories.html
├── static/                # Static files (CSS, JS, images)
│   ├── style.css
│   ├── script.js
├── migrations/            # Database migrations (created by Flask-Migrate)
├── .env                   # Environment variables
├── .venv/                 # Virtual environment directory
├── run.py                 # Entry point for running the application
└── requirements.txt       # Python dependencies
```

---

### 10. Initialize the Flask App

#### `app/__init__.py`
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    from app.models import db
    db.init_app(app)

    from app.schemas import api
    api.init_app(app)

    from app.routes import register_routes
    register_routes(api)

    return app
```

---

## Setup Instructions

### 1. Initialize a Git Repository
1. Create a new directory for the project:
    ```bash
    mkdir pythonFlaskProductCategory
    cd pythonFlaskProductCategory
    ```

2. Initialize a new Git repository:
    ```bash
    git init
    ```

3. Add all project files to the repository:
    ```bash
    git add .
    ```

4. Commit the files:
    ```bash
    git commit -m "Initial commit"
    ```

---

### 2. Set Up the Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the `.env` File
Create a `.env` file in the root directory with the following content:
```dotenv
DATABASE_URI="mysql+mysqlconnector://root:top!secret@localhost:3307/prds"
FLASK_APP=run.py
```

### 5. Initialize the Database
1. Initialize Flask-Migrate:
    ```bash
    flask db init
    ```

2. Create the initial migration:
    ```bash
    flask db migrate -m "Initial migration"
    ```

3. Apply the migration:
    ```bash
    flask db upgrade
    ```

### 6. Run the Application
```bash
flask run
```

The application will be accessible at `http://127.0.0.1:5000/`.

---

### 7. Add Models

#### `app/models/__init__.py`
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

#### `app/models/product.py`
```python
from app.models import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category', back_populates='products')
```

#### `app/models/category.py`
```python
from app.models import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    products = db.relationship('Product', back_populates='category')
```

---

### 8. Add Schemas

#### `app/schemas/__init__.py`
```python
from flask_restx import Api

api = Api(
    title="Product and Category Management API",
    version="1.0",
    description="API for managing products and categories."
)
```

#### `app/schemas/product_schema.py`
```python
from flask_restx import fields
from app.schemas import api

product_model = api.model('Product', {
    'id': fields.Integer(readOnly=True, description='Unique identifier of the product'),
    'name': fields.String(required=True, description='Name of the product'),
    'price': fields.Float(required=True, description='Price of the product'),
    'category': fields.String(attribute='category.name', description='Category of the product')
})
```

#### `app/schemas/category_schema.py`
```python
from flask_restx import fields
from app.schemas import api

category_model = api.model('Category', {
    'id': fields.Integer(readOnly=True, description='Unique identifier of the category'),
    'name': fields.String(required=True, description='Name of the category'),
    'description': fields.String(description='Description of the category')
})
```

---

### 9. Add Routes

#### `app/routes/__init__.py`
```python
def register_routes(api):
    from app.routes.products import product_ns
    from app.routes.categories import category_ns

    api.add_namespace(product_ns)
    api.add_namespace(category_ns)
```

#### `app/routes/products.py`
```python
from flask_restx import Namespace, Resource
from app.models.product import Product
from app.models import db
from app.schemas.product_schema import product_model

product_ns = Namespace('products', description="Product operations")

@product_ns.route('/')
class ProductList(Resource):
    @product_ns.marshal_list_with(product_model)
    def get(self):
        """List all products"""
        return Product.query.all()

    @product_ns.expect(product_model)
    def post(self):
        """Create a new product"""
        data = product_ns.payload
        new_product = Product(
            name=data['name'],
            price=data['price'],
            category_id=data['category']
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product, 201

@product_ns.route('/<int:id>')
class ProductDetail(Resource):
    @product_ns.marshal_with(product_model)
    def get(self, id):
        """Get a product by ID"""
        return Product.query.get_or_404(id)

    def delete(self, id):
        """Delete a product by ID"""
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return '', 204
```

#### `app/routes/categories.py`
```python
from flask_restx import Namespace, Resource
from app.models.category import Category
from app.models import db
from app.schemas.category_schema import category_model

category_ns = Namespace('categories', description="Category operations")

@category_ns.route('/')
class CategoryList(Resource):
    @category_ns.marshal_list_with(category_model)
    def get(self):
        """List all categories"""
        return Category.query.all()

    @category_ns.expect(category_model)
    def post(self):
        """Create a new category"""
        data = category_ns.payload
        new_category = Category(
            name=data['name'],
            description=data.get('description')
        )
        db.session.add(new_category)
        db.session.commit()
        return new_category, 201

@category_ns.route('/<int:id>')
class CategoryDetail(Resource):
    @category_ns.marshal_with(category_model)
    def get(self, id):
        """Get a category by ID"""
        return Category.query.get_or_404(id)

    def delete(self, id):
        """Delete a category by ID"""
        category = Category.query.get_or_404(id)
        db.session.delete(category)
        db.session.commit()
        return '', 204
```

---

### 10. Web Templates

#### `app/templates/base.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Product and Category Management{% endblock %}</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <header>
        <h1>Product and Category Management</h1>
        <nav>
            <a href="/products">Products</a> |
            <a href="/categories">Categories</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```
