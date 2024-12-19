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
## conents of files
### requirments.txt
```txt
alembic==1.14.0
aniso8601==9.0.1
attrs==24.3.0
blinker==1.9.0
click==8.1.7
Flask==3.1.0
Flask-Migrate==4.0.4
flask-restx==1.3.0
Flask-SQLAlchemy==3.1.1
greenlet==3.1.1
importlib_resources==6.4.5
itsdangerous==2.2.0
Jinja2==3.1.4
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
Mako==1.3.8
MarkupSafe==3.0.2
mysql-connector-python==8.0.33
protobuf==3.20.3
python-dotenv==1.0.0
pytz==2024.2
referencing==0.35.1
rpds-py==0.22.3
SQLAlchemy==2.0.36
typing_extensions==4.12.2
Werkzeug==3.1.3
```
### .gitignore
```txt
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
```
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
        source .venv/bin/activate
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
