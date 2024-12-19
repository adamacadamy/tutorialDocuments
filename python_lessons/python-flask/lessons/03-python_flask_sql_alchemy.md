# Flask Food Ordering System with SQLAlchemy ORM, RESTx API, and Migrations

This tutorial demonstrates a modular Flask app structure with scaffolded components for maintainability, scalability, and REST API documentation using Flask-RESTx.

---

## Updated Project Structure

```
food_ordering_app/
├── .gitignore               # Ignore unnecessary files
├── app/                     # Application logic
│   ├── __init__.py          # Initialize Flask app
│   ├── models/              # Folder for database models
│   │   ├── __init__.py      # Initialize SQLAlchemy
│   │   ├── menu_item.py     # MenuItem model
│   │   └── order.py         # Order model
│   ├── routes/              # Folder for application routes
│   │   ├── __init__.py      # Initialize routes
│   │   ├── menu.py          # Menu routes
│   │   └── order.py         # Order routes
├── migrations/              # Flask-Migrate folder
├── .env                     # Store database credentials and configuration
├── .venv/                   # Virtual environment (recommended for dependencies)
├── requirements.txt         # Python dependencies
└── run.py                   # Application entry point
```

---

## Step 1: Define Application Initialization

### `app/__init__.py`
```python
import os
from flask import Flask  
from flask_migrate import Migrate
from flask_restx import Api
from dotenv import load_dotenv
from .models import db
from .routes import register_routes

# Load environmental variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configure MySQL database using .env variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DEV_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)

    # Initialize Flask-RESTx API
    api = Api(
        app,
        version=os.getenv('FOOD_ORDERING_APP_VERSION', '1.0'),
        title=os.getenv('FOOD_ORDERING_APP_TITLE', 'Food Ordering API'),
        description=os.getenv('FOOD_ORDERING_APP_DESCRIPTION', 'API for a food ordering system')
    )

    # Register routes
    register_routes(api)

    return app
```

---

## Step 2: Define Models

### `app/models/__init__.py`
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

### `app/models/menu_item.py`
```python
from . import db

class MenuItem(db.Model):
    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), nullable=False)
    price = db.Column(db.Float, nullable=False)
```

### `app/models/order.py`
```python
from . import db

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(225), nullable=False)
    items = db.Column(db.Text, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
```

---

## Step 3: Define Routes

### `app/routes/__init__.py`
```python
from flask import Blueprint
from .menu import MenuAPI
from .order import OrderAPI

def register_routes(api):
    api.add_resource(MenuAPI, '/menu')
    api.add_resource(OrderAPI, '/order', '/orders')
```

### `app/routes/menu.py`
```python
from flask import request, jsonify
from flask.views import MethodView
from app.models.menu_item import MenuItem
from app.models import db

class MenuAPI(MethodView):
    def get(self):
        menu_items = MenuItem.query.all()
        return jsonify([
            {"id": item.id, "name": item.name, "price": item.price}
            for item in menu_items
        ])

    def post(self):
        data = request.json
        new_item = MenuItem(name=data['name'], price=data['price'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"message": "Menu item added successfully"}), 201
```

### `app/routes/order.py`
```python
from flask import request, jsonify
from flask.views import MethodView
from app.models.order import Order
from app.models.menu_item import MenuItem
from app.models import db

class OrderAPI(MethodView):
    def get(self):
        orders = Order.query.all()
        return jsonify([
            {
                "id": order.id,
                "customer_name": order.customer_name,
                "items": order.items,
                "total_price": order.total_price
            }
            for order in orders
        ])

    def post(self):
        data = request.json
        customer_name = data['customer_name']
        item_ids = data['items']
        items = [MenuItem.query.get(item_id) for item_id in item_ids]
        total_price = sum(item.price for item in items)
        new_order = Order(
            customer_name=customer_name,
            items=','.join(map(str, item_ids)),
            total_price=total_price
        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify({"message": "Order placed successfully", "order_id": new_order.id}), 201
```

---

## Step 4: Using `.env` File

Create a `.env` file in the root directory with the following content:

```
DEV_DATABASE_URI=mysql+mysqlconnector://username:password@localhost/food_ordering
FOOD_ORDERING_APP_VERSION=1.0
FOOD_ORDERING_APP_TITLE=Food Ordering API
FOOD_ORDERING_APP_DESCRIPTION=API for a food ordering system
```

Replace `username` and `password` with your MySQL credentials.

---

## Step 5: Set Up Virtual Environment

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - On Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scriptsctivate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Freeze dependencies to the `requirements.txt` file:
   ```bash
   pip freeze > requirements.txt
   ```

---

## Step 6: Run the Application

### `run.py`
```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```


---

## Step 7: Initialize Migrations
1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

2. **Initialize Flask-Migrate**:
   ```bash
   flask db init
   ```

3. **Generate Migration**:
   ```bash
   flask db migrate -m "Initial migration"
   ```

4. **Apply Migration**:
   ```bash
   flask db upgrade
   ```

5. Start the application:
   ```bash
   python run.py
   ```
---

## Conclusion

This scaffolded structure organizes the Flask app into clearly defined modules with a focus on maintainability. Using Flask-RESTx for API documentation enhances usability, and the modular design ensures scalability.
