
# Responsive Navigation Bar with Collapsing Menu

In this lesson, we will create a responsive navigation bar that collapses into a hamburger menu on small screens using HTML, CSS, and JavaScript.

## Step 1: Basic Structure

We will start by building the basic HTML structure for the navigation bar.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Nav Bar</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="logo">
            <a href="#">Brand</a>
        </div>
        <ul class="nav-links">
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
        <div class="hamburger" onclick="toggleMenu()">
            <span></span>
            <span></span>
            <span></span>
        </div>
    </nav>

    <script src="script.js"></script>
</body>
</html>
```

## Step 2: Basic Styling (CSS)

Now, let's style the navigation bar for larger screens first.

```css
/* General Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
}

/* Navbar Styles */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    padding: 15px;
}

.logo a {
    color: white;
    text-decoration: none;
    font-size: 1.5rem;
}

.nav-links {
    list-style: none;
    display: flex;
}

.nav-links li {
    margin-left: 20px;
}

.nav-links a {
    color: white;
    text-decoration: none;
    font-size: 1.2rem;
}

.hamburger {
    display: none;
    flex-direction: column;
    cursor: pointer;
}

.hamburger span {
    width: 25px;
    height: 3px;
    background-color: white;
    margin: 4px 0;
}

/* Small Screen Styles */
@media (max-width: 768px) {
    .nav-links {
        display: none;
        flex-direction: column;
        width: 100%;
        position: absolute;
        top: 70px;
        left: 0;
        background-color: #333;
    }

    .nav-links li {
        margin: 10px 0;
        text-align: center;
    }

    .hamburger {
        display: flex;
    }
}
```

## Step 3: Adding Interactivity with JavaScript

Now, let's add the functionality to show and hide the nav menu when the hamburger icon is clicked.

```javascript
function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
}
```

### Explanation:

- **HTML:** We have a `nav` element that contains the logo, the navigation links, and a "hamburger" icon.
- **CSS:** The `.navbar` styles handle the basic layout, while the `.nav-links` is hidden on small screens using the `@media` query. The `.hamburger` is styled and shown only on screens smaller than 768px.
- **JavaScript:** The `toggleMenu()` function toggles the visibility of the navigation links on small screens.

### Step 4: Testing

Resize the browser window or open the page on a small screen device. You should see that on small screens, the nav links collapse into a hamburger icon. When the hamburger is clicked, the menu toggles its visibility.
