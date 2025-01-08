# Comprehensive Flask + SQLAlchemy Crash Course
![alt text](images/flask_sqlalchemy.png)
 
---

## **1. Setup and Installation**

1. **Install Required Libraries**

   ```bash
   pip install flask flask-sqlalchemy mysql-connector-python
   ```

2. **Initialize Flask and SQLAlchemy**

   ```python
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:top!secret@localhost:3307/test_1"
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

   db = SQLAlchemy(app)
   app.app_context().push()
   ```

---

## **2. Database Models**

### **Basic Models**

```python
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
```

### **Advanced Models with Relationships**

```python
post_tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tags = db.relationship('Tag', secondary=post_tags, backref='posts', lazy='dynamic')
```

---

## **3. CRUD Operations**

### **Create Tables**

```python
db.create_all()
```

### **Insert Data**

```python
user1 = User(name="Alice", email="alice@example.com")
post1 = Post(title="Flask Basics", content="Intro to Flask", author=user1)
tag1 = Tag(name="Python")

post1.tags.append(tag1)
db.session.add_all([user1, post1, tag1])
db.session.commit()

# Insert Multiple Users
users = [
    User(name="Bob", email="bob@example.com"),
    User(name="Charlie", email="charlie@example.com")
]
db.session.add_all(users)
db.session.commit()
```

### **Query Data**

```python
# Get all users
users = User.query.all()

# Filter users
alice = User.query.filter_by(name="Alice").first()

# Search posts by keyword
posts = Post.query.filter(Post.title.ilike("%Flask%")).all()

# Posts with a specific tag
python_tag = Tag.query.filter_by(name="Python").first()
posts = python_tag.posts.all()
```

### **Update Data**

```python
user = User.query.filter_by(name="Alice").first()
user.email = "alice_new@example.com"
db.session.commit()
```

### **Delete Data**

```python
user = User.query.filter_by(name="Alice").first()
db.session.delete(user)
db.session.commit()
```

---

## **4. Complex Queries**

### **Joins**

```python
# Inner Join: Posts and Authors
results = db.session.query(Post.title, User.name).join(User).all()

# Outer Join: Users and Posts
results = db.session.query(User.name, Post.title).outerjoin(Post).all()
```

### **Aggregations**

```python
from sqlalchemy import func

# Count posts per user
results = db.session.query(User.name, func.count(Post.id)).join(Post).group_by(User.name).all()

# User with the most posts
top_user = db.session.query(User.name, func.count(Post.id).label('post_count'))\
    .join(Post).group_by(User.name).order_by(func.count(Post.id).desc()).first()
```

### **Subqueries**

```python
subquery = db.session.query(Post.id).join(User).filter(User.name == "Alice").subquery()
tags = db.session.query(Tag.name).join(post_tags).filter(post_tags.c.post_id.in_(subquery)).all()
```

---

## **5. Advanced Relationships**

### **Users with a Specific Tag**

```python
python_tag = Tag.query.filter_by(name="Python").first()
users = db.session.query(User.name).join(Post).join(post_tags).filter(post_tags.c.tag_id == python_tag.id).all()
```

### **Posts with Multiple Tags**

```python
python_tag = Tag.query.filter_by(name="Python").first()
flask_tag = Tag.query.filter_by(name="Flask").first()

posts = Post.query.filter(
    Post.tags.contains(python_tag),
    Post.tags.contains(flask_tag)
).all()
```

---

## **6. Pagination**

```python
page = 1
page_size = 5

paginated_posts = Post.query.order_by(Post.id).limit(page_size).offset((page - 1) * page_size).all()
```

---

## **7. Bulk Operations**

### **Bulk Insert**

```python
new_tags = [Tag(name="Django"), Tag(name="REST API"), Tag(name="Machine Learning")]
db.session.bulk_save_objects(new_tags)
db.session.commit()
```

### **Bulk Update**

```python
default_tag = Tag.query.filter_by(name="General").first()
posts = Post.query.all()
for post in posts:
    post.tags.append(default_tag)

db.session.commit()
```

---

## **8. Transaction Management**

```python
from sqlalchemy.exc import SQLAlchemyError

try:
    user = User(name="Charlie", email="charlie@example.com")
    db.session.add(user)

    post = Post(title="Transaction Safety", content="SQLAlchemy is robust.", author=user)
    db.session.add(post)

    db.session.commit()
except SQLAlchemyError as e:
    db.session.rollback()
    print(f"Transaction failed: {e}")
```

---

## **9. Best Practices**

1. **Lazy vs. Eager Loading**

   ```python
   posts_with_tags = Post.query.options(db.joinedload(Post.tags)).all()
   ```

2. **Indexing**

   ```python
   email = db.Column(db.String(100), index=True)
   ```

3. **Error Handling**
   Wrap operations in `try-except` blocks to handle database errors gracefully.

---

 