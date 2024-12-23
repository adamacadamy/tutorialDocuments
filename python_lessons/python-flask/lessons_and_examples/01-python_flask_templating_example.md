# Flask Food Ordering System with SQLAlchemy ORM and Migrations (Scaffolded Modular Structure)

This tutorial demonstrates a highly modular Flask app structure with scaffolded components for maintainability and scalability.

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
│   └── routes/              # Folder for application routes
│       ├── __init__.py      # Initialize routes
│       ├── menu.py          # Menu routes
│       ├── order.py         # Order routes
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
from dotenv import load_dotenv
from app.models import db
from app.routes import register_routes

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configure MySQL database using .env variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)

    # Register routes
    register_routes(app)

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
from app.models import db

class MenuItem(db.Model):
    __tablename__ = 'menu_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
```

### `app/models/order.py`
```python
from app.models import db

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255), nullable=False)
    items = db.Column(db.Text, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
```

---

## Step 3: Define Routes

### `app/routes/__init__.py`
```python
def register_routes(app):
    from app.routes.menu import menu_bp
    from app.routes.order import order_bp

    app.register_blueprint(menu_bp, url_prefix="/menu")
    app.register_blueprint(order_bp, url_prefix="/order")
```

### `app/routes/menu.py`
```python
from flask import Blueprint, jsonify, request
from app.models.menu_item import MenuItem
from app.models import db

menu_bp = Blueprint('menu', __name__)

@menu_bp.route('/', methods=['GET'])
def get_menu():
    menu_items = MenuItem.query.all()
    return jsonify([{"id": item.id, "name": item.name, "price": item.price} for item in menu_items])

@menu_bp.route('/', methods=['POST'])
def add_menu_item():
    data = request.json
    new_item = MenuItem(name=data['name'], price=data['price'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Menu item added successfully"}), 201
```

### `app/routes/order.py`
```python
from flask import Blueprint, jsonify, request
from app.models.order import Order
from app.models.menu_item import MenuItem
from app.models import db

order_bp = Blueprint('order', __name__)

@order_bp.route('/', methods=['POST'])
def place_order():
    data = request.json
    customer_name = data['customer_name']
    items = data['items']
    total_price = sum(MenuItem.query.get(item_id).price for item_id in items)
    new_order = Order(customer_name=customer_name, items=",".join(map(str, items)), total_price=total_price)
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order placed successfully", "order_id": new_order.id}), 201

@order_bp.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        "id": order.id,
        "customer_name": order.customer_name,
        "items": order.items,
        "total_price": order.total_price
    } for order in orders])
```

---

## Step 4: Using `.env` File

Create a `.env` file in the root directory with the following content:

```
DATABASE_URI=mysql+mysqlconnector://username:password@localhost/food_ordering
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
     .venv\Scripts\activate
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

## Step 6: Initialize Migrations

1. **Initialize Flask-Migrate**:
   ```bash
   flask db init
   ```

2. **Generate Migration**:
   ```bash
   flask db migrate -m "Initial migration"
   ```

3. **Apply Migration**:
   ```bash
   flask db upgrade
   ```

---

## Step 7: Run the Application

### `run.py`
```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

1. Activate the virtual environment:
   - On Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

2. Start the application:
   ```bash
   python run.py
   ```

---

## Step 8: Add `.gitignore` File

Create a `.gitignore` file in the root directory with the following content:

```
# Ignore virtual environment
.venv/

# Ignore environment variables
.env

# Ignore compiled Python files
__pycache__/
*.pyc

# Ignore migrations folder cache
migrations/versions/
```

---

## Conclusion

This scaffolded structure organizes the Flask app into clearly defined modules with a focus on maintainability. Using `.gitignore` prevents unnecessary files from being tracked in version control, and the modular design ensures scalability.


## reference code
