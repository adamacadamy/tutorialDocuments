# Flask Beginner Tutorial: From Scaffolding to a Basic Application (Updated with Class-Based Routes)

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
#### Using Class-Based Routes
```python
# app/routes.py
from flask import render_template
from flask.views import MethodView

class HomeView(MethodView):
    def get(self):
        return "Welcome to Flask!"

class AboutView(MethodView):
    def get(self):
        return "This is the about page."

def register_routes(app):
    app.add_url_rule("/", view_func=HomeView.as_view("home"))
    app.add_url_rule("/about", view_func=AboutView.as_view("about"))
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

### Update `routes.py` with Class-Based Views
```python
from flask import render_template
from flask.views import MethodView

class HomeView(MethodView):
    def get(self):
        return render_template("home.html", title="Home")

class AboutView(MethodView):
    def get(self):
        return render_template("about.html", title="About")

def register_routes(app):
    app.add_url_rule("/", view_func=HomeView.as_view("home"))
    app.add_url_rule("/about", view_func=AboutView.as_view("about"))
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

### Update `routes.py` with Class-Based Views
```python
from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from app.forms import ContactForm

class ContactView(MethodView):
    def get(self):
        form = ContactForm()
        return render_template("contact.html", title="Contact", form=form)

    def post(self):
        form = ContactForm()
        if form.validate_on_submit():
            flash(f"Message from {form.name.data} sent!")
            return redirect(url_for("contact"))
        return render_template("contact.html", title="Contact", form=form)

def register_routes(app):
    app.add_url_rule("/", view_func=HomeView.as_view("home"))
    app.add_url_rule("/about", view_func=AboutView.as_view("about"))
    app.add_url_rule("/contact", view_func=ContactView.as_view("contact"), methods=["GET", "POST"])
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

This updated tutorial provides a strong foundation for building Flask applications using class-based views. Let me know if you need more examples or want to explore advanced features!
