
# Responsive Navbar with Breadcrumbs (No JS) - Brand Disappearing or Moving Above Menu

In this tutorial, we will create a responsive navbar with breadcrumbs using only HTML and CSS. You will also learn how to make the brand (logo) either disappear or move above the menu when the navbar collapses in mobile view. This approach requires no JavaScript.

## HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Navbar with Breadcrumbs (No JS)</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar">
        <div class="navbar-container">
            <a href="#" class="brand">MyBrand</a>
            <input type="checkbox" id="menu-toggle">
            <label for="menu-toggle" class="navbar-toggle">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </label>
            <ul class="nav-menu">
                <li class="nav-item"><a href="#">Home</a></li>
                <li class="nav-item"><a href="#">Services</a></li>
                <li class="nav-item"><a href="#">About</a></li>
                <li class="nav-item"><a href="#">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Breadcrumb -->
    <div class="breadcrumb">
        <a href="#">Home</a> > 
        <a href="#">Category</a> > 
        <a href="#">Sub-category</a> > 
        <span>Current Page</span>
    </div>

</body>
</html>
```

## CSS for Disappearing Brand and Updated Breadcrumb Style

The following CSS makes the brand disappear when the navbar collapses in mobile view and adjusts the breadcrumb style as requested.

```css
/* General Styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.navbar {
    background-color: #333;
    position: relative;
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.navbar-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-menu {
    list-style: none;
    display: flex;
    gap: 15px;
}

.nav-item a {
    color: white;
    text-decoration: none;
    padding: 8px 12px;
    transition: background-color 0.3s;
}

.nav-item a:hover {
    background-color: #555;
}

.brand {
    color: white;
    text-decoration: none;
    font-size: 24px;
    font-weight: bold;
}

/* Updated Breadcrumb Style */
.breadcrumb {
    background-color: #f8f9fa;
    padding: 5px 10px;
    border-radius: 5px;
}

.breadcrumb a {
    color: #007bff;
    text-decoration: none;
}

.breadcrumb span {
    color: #6c757d;
}

/* Hide checkbox (for menu toggling) */
#menu-toggle {
    display: none;
}

/* Mobile Menu Toggle */
.navbar-toggle {
    display: none;
    flex-direction: column;
    cursor: pointer;
}

.navbar-toggle .bar {
    width: 25px;
    height: 3px;
    background-color: white;
    margin: 3px 0;
}

/* Mobile Menu */
@media screen and (max-width: 768px) {
    .nav-menu {
        display: none;
        flex-direction: column;
        width: 100%;
        background-color: #333;
    }

    .nav-item {
        text-align: center;
        padding: 10px 0;
    }

    .navbar-toggle {
        display: flex;
    }

    /* Move brand above the menu */
    .navbar-container {
        flex-direction: column;
        align-items: flex-start;
    }

    /* Hide brand when breadcrumb is visible (in mobile view) */
    .brand {
        display: none;
    }

    /* Show breadcrumb on the left in mobile view */
    .breadcrumb {
        position: relative;
        top: 0;
        right: auto;
        left: 20px;
        margin-top: 10px;
    }

    /* Show the menu when the checkbox is checked */
    #menu-toggle:checked + .navbar-toggle + .nav-menu {
        display: flex;
    }
}

/* Breadcrumb + Brand Interaction on Larger Screens */
@media screen and (min-width: 769px) {
    /* Show breadcrumb on the right in larger screens */
    .breadcrumb {
        display: block;
        position: absolute;
        top: 10px;
        right: 20px;
    }

    /* Hide the brand when the breadcrumb is visible */
    .navbar .breadcrumb ~ .brand {
        display: none;
    }
}
```

### Explanation

- **Updated Breadcrumb Style**: The breadcrumb has a background color of `#f8f9fa`, padding of `5px 10px`, and a border-radius of `5px`. Links inside the breadcrumb have a blue color `#007bff`, and the current page is displayed in gray (`#6c757d`).
- **Hide Brand on Mobile**: The brand disappears when the screen width is less than `768px` and the breadcrumb is visible.
- **Positioning Breadcrumb**: The breadcrumb is placed at the top right on larger screens and moves to the left in mobile view.

## Conclusion

This tutorial demonstrates how to create a responsive navbar with breadcrumbs using only HTML and CSS, without relying on JavaScript. You have the option to either make the brand disappear or move it above the menu when the navbar collapses in mobile view.
