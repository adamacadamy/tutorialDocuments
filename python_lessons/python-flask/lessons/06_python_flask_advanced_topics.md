
# **Advanced Flask Tutorial**

---

## **1. Class-Based Routes**

Class-based routes in Flask allow you to organize your logic into classes rather than functions. Flask provides `MethodView` to handle routes for different HTTP methods.

### **Example: Using MethodView**

#### **Code: Class-Based Routes**
```python
from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)

class ItemAPI(MethodView):
    items = {}

    def get(self, item_id=None):
        if item_id is None:
            return jsonify(self.items)
        return jsonify(self.items.get(item_id, "Item not found"))

    def post(self):
        data = request.json
        item_id = len(self.items) + 1
        self.items[item_id] = data
        return jsonify({"id": item_id, "data": data}), 201

    def delete(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            return jsonify({"message": "Item deleted"}), 200
        return jsonify({"error": "Item not found"}), 404

# Register the class-based view
item_view = ItemAPI.as_view("item_api")
app.add_url_rule("/items", defaults={"item_id": None}, view_func=item_view, methods=["GET", "POST"])
app.add_url_rule("/items/<int:item_id>", view_func=item_view, methods=["GET", "DELETE"])

if __name__ == "__main__":
    app.run(debug=True)
```

---

## **2. Token-Based Authentication**

Token authentication secures your API by requiring a valid token for requests. You can use **PyJWT** to generate and validate tokens.

### **Setup**

1. Install PyJWT:
   ```bash
   pip install pyjwt
   ```

2. Implement token authentication.

### **Example: Token Authentication with PyJWT**
```python
import jwt
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"

# Generate a token
@app.route("/login", methods=["POST"])
def login():
    auth = request.json
    if auth.get("username") == "admin" and auth.get("password") == "password":
        token = jwt.encode(
            {"user": auth["username"], "exp": datetime.utcnow() + timedelta(hours=1)},
            app.config["SECRET_KEY"],
            algorithm="HS256",
        )
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

# Token-protected route
@app.route("/protected", methods=["GET"])
def protected():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token is missing"}), 401
    try:
        jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        return jsonify({"message": "This is a protected route"})
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

if __name__ == "__main__":
    app.run(debug=True)
```

---

## **3. Middleware in Flask**

Middleware is used to execute code **before** or **after** each request. Flask provides hooks like `@app.before_request` and `@app.after_request` for middleware-like behavior.

### **Example: Logging Middleware**
```python
from flask import Flask, request

app = Flask(__name__)

@app.before_request
def log_request():
    print(f"Request Method: {request.method}")
    print(f"Request Path: {request.path}")
    print(f"Request Headers: {dict(request.headers)}")

@app.after_request
def log_response(response):
    print(f"Response Status: {response.status}")
    return response

@app.route("/")
def index():
    return "Welcome to Middleware Example!"

if __name__ == "__main__":
    app.run(debug=True)
```

---

### **Example: API Rate Limiting Middleware**
```python
from flask import Flask, request, jsonify
from time import time

app = Flask(__name__)

# Store request timestamps for each client IP
request_times = {}
RATE_LIMIT = 5  # Allow 5 requests per minute

@app.before_request
def rate_limit():
    client_ip = request.remote_addr
    current_time = time()
    timestamps = request_times.get(client_ip, [])

    # Keep only timestamps within the last minute
    timestamps = [t for t in timestamps if current_time - t < 60]
    request_times[client_ip] = timestamps

    if len(timestamps) >= RATE_LIMIT:
        return jsonify({"error": "Rate limit exceeded"}), 429

    # Log the current request time
    request_times[client_ip].append(current_time)

@app.route("/")
def home():
    return jsonify({"message": "Welcome! You are within the rate limit."})

if __name__ == "__main__":
    app.run(debug=True)
```

---

## **4. Flask and WebSockets**

Flask-SocketIO enables real-time communication using WebSockets.

### **Setup**

1. Install Flask-SocketIO:
   ```bash
   pip install flask-socketio
   ```

### **Example: WebSocket Chat Application**
```python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("chat.html")

@socketio.on("join")
def on_join(data):
    username = data["username"]
    room = data["room"]
    join_room(room)
    emit("message", {"user": "System", "message": f"{username} has joined the room."}, room=room)

@socketio.on("leave")
def on_leave(data):
    username = data["username"]
    room = data["room"]
    leave_room(room)
    emit("message", {"user": "System", "message": f"{username} has left the room."}, room=room)

@socketio.on("message")
def handle_message(data):
    room = data["room"]
    emit("message", {"user": data["username"], "message": data["message"]}, room=room)

if __name__ == "__main__":
    socketio.run(app, debug=True)
```

#### **Template: `chat.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Flask Chat</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.0/socket.io.js"></script>
</head>
<body>
    <h1>Chat Application</h1>
    <form id="joinForm">
        Username: <input id="username" required>
        Room: <input id="room" required>
        <button type="submit">Join</button>
    </form>

    <div id="chatBox" style="display: none;">
        <h2>Chat Room: <span id="roomName"></span></h2>
        <ul id="messages"></ul>
        <form id="messageForm">
            <input id="messageInput" required>
            <button type="submit">Send</button>
        </form>
        <button id="leave">Leave Room</button>
    </div>

    <script>
        const socket = io();

        const joinForm = document.getElementById("joinForm");
        const chatBox = document.getElementById("chatBox");
        const messages = document.getElementById("messages");
        const roomName = document.getElementById("roomName");
        const leaveButton = document.getElementById("leave");

        joinForm.addEventListener("submit", (e) => {
            e.preventDefault();
            const username = document.getElementById("username").value;
            const room = document.getElementById("room").value;
            socket.emit("join", { username, room });
            chatBox.style.display = "block";
            joinForm.style.display = "none";
            roomName.textContent = room;
        });

        leaveButton.addEventListener("click", () => {
            const username = document.getElementById("username").value;
            const room = roomName.textContent;
            socket.emit("leave", { username, room });
            chatBox.style.display = "none";
            joinForm.style.display = "block";
        });

        document.getElementById("messageForm").addEventListener("submit", (e) => {
            e.preventDefault();
            const message = document.getElementById("messageInput").value;
            const username = document.getElementById("username").value;
            const room = roomName.textContent;
            socket.emit("message", { username, message, room });
            document.getElementById("messageInput").value = "";
        });

        socket.on("message", (data) => {
            const item = document.createElement("li");
            item.textContent = `${data.user}: ${data.message}`;
            messages.appendChild(item);
        });
    </script>
</body>
</html>
```

---
