# Flask Example: Forms with Models

## Overview
This example demonstrates how to use Flask-WTF forms for handling user input and integrate it with SQLAlchemy models for data storage. The application includes:
- Flask-WTF for form handling
- SQLAlchemy models for database interactions
- Web-based user registration and login forms
- A "Contact Us" page

---

## Project Structure

The application follows this structure:

```
├── .gitignore               # Ignore unnecessary files
├── app/                     # Application logic
│   ├── __init__.py          # Initialize Flask app
│   ├── models/              # Folder for database models
│   │   ├── __init__.py      # Initialize SQLAlchemy
│   │   ├── user.py          # User model
│   ├── forms/               # Folder for Flask-WTF forms
│   │   ├── __init__.py      # Initialize forms
│   │   ├── registration_form.py  # Registration form
│   │   ├── login_form.py         # Login form
│   │   ├── contact_form.py       # Contact page form
│   ├── routes/              # Folder for application routes
│   │   ├── __init__.py      # Initialize routes
│   │   ├── auth.py          # Authentication routes
│   │   ├── contact.py       # Contact page route
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── register.html        # Registration template
│   ├── login.html           # Login template
│   ├── contact.html         # Contact page template
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

## Step 1: Application Setup

### `run.py`
```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
```

---

## Step 2: Initialize Flask App

### `app/__init__.py`
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:password@localhost/flask_forms"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "your_secret_key"

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import register_blueprints
    register_blueprints(app)

    return app
```

---

## Step 3: Database Models

### `app/models/__init__.py`
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

### `app/models/user.py`
```python
from app.models import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def create_user(username, email, password):
        hashed_password = generate_password_hash(password)
        return User(username=username, email=email, password_hash=hashed_password)
```

---

## Step 4: Forms

### `app/forms/__init__.py`
```python
# Placeholder for forms package
```

### `app/forms/registration_form.py`
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")
```

### `app/forms/login_form.py`
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
```

### `app/forms/contact_form.py`
```python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators = DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField("Send Message")
```

---

## Step 5: Routes

### `app/routes/__init__.py`
```python
def register_blueprints(app):
    from app.routes.auth import auth_bp
    from app.routes.contact import contact_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(contact_bp, url_prefix="/contact")
```

### `app/routes/contact.py`
```python
from flask import Blueprint, render_template, flash, redirect, url_for
from app.forms.contact_form import ContactForm

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # Process the form data (e.g., send email, save to database)
        flash("Your message has been sent successfully!", "success")
        return redirect(url_for("contact.contact"))

    return render_template("contact.html", form=form)
```

---

## Step 6: Templates

### `templates/base.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Flask Forms{% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <script src="/static/script.js"></script>
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

### `templates/register.html`
```html
{% extends "base.html" %}
{% block title %}Register{% endblock %}
{% block content %}
<h2>Register</h2>
<form method="POST">
    {{ form.hidden_tag() }}
    <div>{{ form.username.label }} {{ form.username }}</div>
    <div>{{ form.email.label }} {{ form.email }}</div>
    <div>{{ form.password.label }} {{ form.password }}</div>
    <div>{{ form.confirm_password.label }} {{ form.confirm_password }}</div>
    <div>{{ form.submit }}</div>
</form>
{% endblock %}
```

### `templates/login.html`
```html
{% extends "base.html" %}
{% block title %}Login{% endblock %}
{% block content %}
<h2>Login</h2>
<form method="POST">
    {{ form.hidden_tag() }}
    <div>{{ form.email.label }} {{ form.email }}</div>
    <div>{{ form.password.label }} {{ form.password }}</div>
    <div>{{ form.submit }}</div>
</form>
{% endblock %}
```

### `templates/contact.html`
```html
{% extends "base.html" %}
{% block title %}Contact Us{% endblock %}
{% block content %}
<h2>Contact Us</h2>
<form method="POST">
    {{ form.hidden_tag() }}
    <div>{{ form.name.label }} {{ form.name }}</div>
    <div>{{ form.email.label }} {{ form.email }}</div>
    <div>{{ form.message.label }} {{ form.message }}</div>
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
    background-color: #f8f9fa;
}

.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: #fff;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

### `static/script.js`
```javascript
document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript is connected.');
});
```

---

## Step 8: Environment Configuration

### `.env`
```
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://root:top!secret@localhost/flask_forms
SQLALCHEMY_TRACK_MODIFICATIONS=False
```

---

## Step 9: Requirements

### `requirements.txt`
```
alembic==1.14.0
aniso8601==9.0.1
attrs==24.3.0
blinker==1.9.0
click==8.1.8
Flask==3.1.0
Flask-Migrate==4.0.7
Flask-WTF
flask-restx==1.3.0
Flask-SQLAlchemy==3.1.1
greenlet==3.1.1
importlib_resources==6.4.5
itsdangerous==2.2.0
Jinja2==3.1.5
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
Mako==1.3.8
MarkupSafe==3.0.2
mysql-connector-python==9.1.0
python-dotenv==1.0.1
pytz==2024.2
referencing==0.35.1
rpds-py==0.22.3
SQLAlchemy==2.0.36
typing_extensions==4.12.2
Werkzeug==3.1.3
```

## Step 10: Migration Commands

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
   
