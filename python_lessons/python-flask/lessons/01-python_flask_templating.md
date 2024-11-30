
# Flask Beginner Tutorial: From Scaffolding to a Basic Application

## 1. Setting Up the Environment

### Install Flask
1. Create a virtual environment:
   ```bash
   python -m venv flask_env
   source flask_env/bin/activate  # On Windows: flask_env\Scripts\activate
   ```

2. Install Flask:
   ```bash
   pip install flask
   ```

### Create Project Structure
Organize your project as follows:
```
flask_project/
├── app/
│   ├── __init__.py
│   ├── routes.py
├── run.py
├── requirements.txt
```

---

## 2. Basic Flask Application

### Initialize Flask in `__init__.py`
```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    return app
```

### Define Routes in `routes.py`
```python
# app/routes.py
from flask import Flask, render_template

def register_routes(app):
    @app.route("/")
    def home():
        return "Welcome to Flask!"

    @app.route("/about")
    def about():
        return "This is the about page."
```

### Wire It Together in `run.py`
```python
# run.py
from app import create_app
from app.routes import register_routes

app = create_app()
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
```

### Install Dependencies
Save your dependencies:
```bash
pip freeze > requirements.txt
```

### Run the Application
```bash
python run.py
```
Visit `http://127.0.0.1:5000` in your browser.

---

## 3. Adding HTML Templates

### Add a `templates/` Folder
Create the following structure:
```
flask_project/
├── app/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
```

### Create `base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a> |
            <a href="/about">About</a>
        </nav>
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>
```

### Create `home.html`
```html
{% extends "base.html" %}
{% block content %}
<h1>Welcome to Flask</h1>
<p>This is the home page.</p>
{% endblock %}
```

### Create `about.html`
```html
{% extends "base.html" %}
{% block content %}
<h1>About Page</h1>
<p>This is the about page.</p>
{% endblock %}
```

### Update `routes.py`
```python
from flask import render_template

def register_routes(app):
    @app.route("/")
    def home():
        return render_template("home.html", title="Home")

    @app.route("/about")
    def about():
        return render_template("about.html", title="About")
```

---

## 4. Adding Static Files

### Add a `static/` Folder
```
flask_project/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   ├── styles.css
```

### Create `styles.css`
```css
/* app/static/css/styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 0;
}

header {
    margin-bottom: 20px;
}

nav a {
    text-decoration: none;
    margin-right: 10px;
    color: blue;
}

nav a:hover {
    text-decoration: underline;
}
```

### Link CSS in `base.html`
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
```

---

## 5. Adding Forms

### Install Flask-WTF
```bash
pip install flask-wtf
```

### Create a Contact Form
```python
# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")
```

### Update `routes.py`
```python
from flask import request, redirect, url_for, flash
from app.forms import ContactForm

def register_routes(app):
    app.secret_key = "secret_key"  # Replace with a secure key

    @app.route("/")
    def home():
        return render_template("home.html", title="Home")

    @app.route("/about")
    def about():
        return render_template("about.html", title="About")

    @app.route("/contact", methods=["GET", "POST"])
    def contact():
        form = ContactForm()
        if form.validate_on_submit():
            flash(f"Message from {form.name.data} sent!")
            return redirect(url_for("contact"))
        return render_template("contact.html", title="Contact", form=form)
```

### Create `contact.html`
```html
{% extends "base.html" %}
{% block content %}
<h1>Contact Us</h1>
<form method="POST">
    {{ form.hidden_tag() }}
    <p>{{ form.name.label }} {{ form.name }}</p>
    <p>{{ form.message.label }} {{ form.message }}</p>
    <p>{{ form.submit }}</p>
</form>
{% for message in get_flashed_messages() %}
    <p style="color: green;">{{ message }}</p>
{% endfor %}
{% endblock %}
```

---

## 6. Next Steps

- **Explore Flask extensions**:
  - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/): For database integration.
  - [Flask-Migrate](https://flask-migrate.readthedocs.io/): For database migrations.
  - [Flask-Login](https://flask-login.readthedocs.io/): For user authentication.

- **Learn Deployment**:
  Deploy your app to [Heroku](https://www.heroku.com/) or [AWS](https://aws.amazon.com/).

---

This tutorial provides a strong foundation for building Flask applications. Let me know if you need more details or want to explore advanced features!
