# Flask Food Ordering System with SQLAlchemy ORM and Migrations

## Overview
This tutorial demonstrates a modular Flask app structure with scaffolded components for a food ordering system, utilizing Flask-RESTx for building APIs, SQLAlchemy for ORM, and web views for interacting with the APIs.

---

## Project Structure

```
├── .gitignore               # Ignore unnecessary files
├── app/                     # Application logic
│   ├── __init__.py          # Initialize Flask app
│   ├── models/              # Folder for database models
│   │   ├── __init__.py      # Initialize SQLAlchemy
│   │   ├── menu_item.py     # MenuItem model
│   │   └── order.py         # Order model
│   ├── routes/              # Application routes
│   │   ├── __init__.py      # Initialize routes
│   │   ├── menu.py          # Menu routes
│   │   ├── order.py         # Order routes
│   ├── schemas/             # API schemas
│   │   ├── __init__.py      # Initialize schemas
│   │   ├── menu_schema.py   # Schema for menu item
│   │   └── order_schema.py  # Schema for order
│   ├── forms/               # Web forms for interacting with the API
│   │   ├── __init__.py      # Initialize forms
│   │   ├── menu_form.py     # Form for menu items
│   │   └── order_form.py    # Form for orders
│   ├── templates/           # HTML templates for web views
│       ├── base.html        # Base template
│       ├── menu.html        # Menu template
│       ├── order.html       # Order template
├── static/                  # Static files (CSS, JS, images)
│   ├── style.css            # Stylesheet
│   ├── script.js            # JavaScript file
├── migrations/              # Flask-Migrate folder
├── .env                     # Store database credentials and configuration
├── .venv/                   # Virtual environment (recommended for dependencies)
├── requirements.txt         # Python dependencies
└── run.py                   # Application entry point
```

---

## Step 1: Application Initialization

### `app/__init__.py`
```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from .routes import register_routes
from .schemas import api
from .models import db
# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    Migrate(app, db)
    api.init_app(app)
    register_routes(api)

    return app
```

---

## Step 2: Database Models

### `app/models/__init__.py`
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

### `app/models/menu_item.py`
```python
from app.models import db

class MenuItem(db.Model):
    __tablename__ = "menu_items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
```

### `app/models/order.py`
```python
from app.models import db

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255), nullable=False)
    items = db.Column(db.Text, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
```

---

## Step 3: Routes

### `app/routes/__init__.py`
```python
def register_routes(api):
    from app.routes.menu import menu_ns
    from app.routes.order import order_ns

    api.add_namespace(menu_ns, path="/menu")
    api.add_namespace(order_ns, path="/order")
```

### `app/routes/menu.py`
```python
from flask_restx import Namespace, Resource
from flask import request
from app.models.menu_item import MenuItem
from app.models import db
from app.schemas.menu_schema import menu_item_model

menu_ns = Namespace("Menu", description="Menu management")

@menu_ns.route("/")
class MenuList(Resource):
    @menu_ns.marshal_list_with(menu_item_model)
    def get(self):
        """List all menu items."""
        return MenuItem.query.all()

    @menu_ns.expect(menu_item_model)
    def post(self):
        """Add a new menu item."""
        data = request.json
        new_item = MenuItem(name=data["name"], price=data["price"])
        db.session.add(new_item)
        db.session.commit()
        return {"message": "Menu item added successfully."}, 201
```

### `app/routes/order.py`
```python
from flask_restx import Namespace, Resource
from flask import request
from app.models.order import Order
from app.models.menu_item import MenuItem
from app.models import db
from app.schemas.order_schema import order_model

order_ns = Namespace("Order", description="Order management")

@order_ns.route("/")
class OrderList(Resource):
    @order_ns.marshal_with(order_model, as_list=True)
    def get(self):
        """List all orders."""
        return Order.query.all()

    @order_ns.expect(order_model)
    def post(self):
        """Place a new order."""
        data = request.json
        customer_name = data["customer_name"]
        items = data["items"]
        total_price = sum(MenuItem.query.get(item_id).price for item_id in items)
        new_order = Order(customer_name=customer_name, items=",".join(map(str, items)), total_price=total_price)
        db.session.add(new_order)
        db.session.commit()
        return {"message": "Order placed successfully.", "order_id": new_order.id}, 201
```

---

## Step 4: API Schemas

### `app/schemas/__init__.py`
```python
from flask_restx import Api

api = Api(
    title="Food Ordering System API",
    version="1.0",
    description="An API for managing menu items and orders."
)
```

### `app/schemas/menu_schema.py`
```python
from flask_restx import fields
from app.schemas import api

menu_item_model = api.model(
    "MenuItem",
    {
        "id": fields.Integer(readonly=True, description="Menu item ID"),
        "name": fields.String(required=True, description="Menu item name"),
        "price": fields.Float(required=True, description="Menu item price")
    }
)
```

### `app/schemas/order_schema.py`
```python
from flask_restx import fields
from app.schemas import api

order_model = api.model(
    "Order",
    {
        "id": fields.Integer(readonly=True, description="Order ID"),
        "customer_name": fields.String(required=True, description="Customer name"),
        "items": fields.List(fields.Integer, required=True, description="List of menu item IDs"),
        "total_price": fields.Float(readonly=True, description="Total order price")
    }
)
```

---

## Step 5: Web Forms

### `app/forms/__init__.py`
```python
# Placeholder for forms package
```

### `app/forms/menu_form.py`
```python
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class MenuItemForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    submit = SubmitField("Add Item")
```

### `app/forms/order_form.py`
```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired

class OrderForm(FlaskForm):
    customer_name = StringField("Customer Name", validators=[DataRequired()])
    items = FieldList(StringField("Item ID", validators=[DataRequired()]), min_entries=1)
    submit = SubmitField("Place Order")
```

---

## Step 6: Templates

### `app/templates/base.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Food Ordering System{% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <header>
        <h1>Food Ordering System</h1>
        <nav>
            <a href="/menu">Menu</a> | <a href="/order">Orders</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <script src="/static/script.js"></script>
</body>
</html>
```

### `app/templates/menu.html`
```html
{% extends "base.html" %}
{% block title %}Menu{% endblock %}
{% block content %}
<h2>Menu</h2>
<form method="POST">
    {{ form.hidden_tag() }}
    <div>{{ form.name.label }} {{ form.name }}</div>
    <div>{{ form.price.label }} {{ form.price }}</div>
    <div>{{ form.submit }}</div>
</form>
{% endblock %}
```

### `app/templates/order.html`
```html
{% extends "base.html" %}
{% block title %}Orders{% endblock %}
{% block content %}
<h2>Place an Order</h2>
<form method="POST">
    {{ form.hidden_tag() }}
    <div>{{ form.customer_name.label }} {{ form.customer_name }}</div>
    <div>{{ form.items.label }}
        {% for field in form.items %}
            {{ field }}
        {% endfor %}
    </div>
    <div>{{ form.submit }}</div>
</form>
{% endblock %}
```

---

## Step 7: Static Files

### `static/style.css`
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
}

header {
    background-color: #333;
    color: white;
    padding: 10px 20px;
    text-align: center;
}

header h1 {
    margin: 0;
    font-size: 24px;
}

header nav {
    margin-top: 10px;
}

header nav a {
    color: white;
    text-decoration: none;
    margin: 0 10px;
    font-size: 18px;
}

header nav a:hover {
    text-decoration: underline;
}

main {
    margin: 20px auto;
    max-width: 800px;
    padding: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

h2 {
    color: #333;
    font-size: 22px;
    margin-bottom: 20px;
}

form div {
    margin-bottom: 15px;
}

form label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
}

form input, form select {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
}

form input[type="submit"] {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
}

form input[type="submit"]:hover {
    background-color: #0056b3;
}
```

---

### `static/script.js`
```javascript
document.addEventListener("DOMContentLoaded", () => {
    console.log("JavaScript is working!");
});
```


## Step 8: Migration Commands

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
   
