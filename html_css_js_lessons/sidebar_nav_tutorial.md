
# Sidebar Navigation with Submenus and Linked Main Menu in HTML and CSS

In this tutorial, we will create a sidebar navigation menu with both main menu links and expandable submenus using HTML and CSS.

## Step 1: HTML Structure

First, we create the basic structure for our sidebar and content area. The sidebar will contain main menu items, each with links, and some will have dropdown submenus.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sidebar Navigation with Linked Main Menus</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <div class="sidebar">
    <a href="#home">Home</a>

    <div class="dropdown">
      <a href="#services" class="main-menu">Services</a>
      <div class="dropdown-content">
        <a href="#web">Web Development</a>
        <a href="#mobile">Mobile Development</a>
        <a href="#design">UI/UX Design</a>
      </div>
    </div>

    <div class="dropdown">
      <a href="#about" class="main-menu">About</a>
      <div class="dropdown-content">
        <a href="#team">Our Team</a>
        <a href="#company">Our Company</a>
      </div>
    </div>

    <a href="#contact">Contact</a>
  </div>

  <div class="content">
    <h1>Welcome to the Website</h1>
    <p>This is the main content area.</p>
  </div>

</body>
</html>
```

### Explanation:

- The sidebar contains several links: **Home**, **Services** (with a submenu), **About** (with a submenu), and **Contact**.
- The `dropdown` class is used to define the dropdown container for the submenus.
- The `dropdown-content` contains the links that are part of the submenu.
- The `main-menu` class is applied to the main menu items that have submenus.

---

## Step 2: CSS for Styling

Next, we add the CSS to style the sidebar, the dropdown menus, and ensure the submenus are hidden until hovered over.

```css
/* General styles */
body {
  margin: 0;
  font-family: Arial, sans-serif;
}

/* Sidebar styles */
.sidebar {
  height: 100%;
  width: 250px;
  position: fixed;
  top: 0;
  left: 0;
  background-color: #111;
  padding-top: 20px;
}

.sidebar a {
  padding: 15px 10px;
  text-decoration: none;
  font-size: 18px;
  color: white;
  display: block;
}

.sidebar a:hover {
  background-color: #575757;
  color: #f1f1f1;
}

/* Dropdown container */
.dropdown {
  position: relative;
}

.dropdown-content {
  display: none;
  background-color: #333;
  padding-left: 20px;
}

.dropdown-content a {
  padding: 10px 10px;
  font-size: 16px;
  display: block;
  color: white;
}

.dropdown-content a:hover {
  background-color: #575757;
}

/* Show the dropdown on hover */
.dropdown:hover .dropdown-content {
  display: block;
}

/* Make main menu links clickable and distinguishable */
.main-menu {
  position: relative;
  cursor: pointer;
}

.main-menu::after {
  content: ' ▼';
  font-size: 12px;
  position: absolute;
  right: 10px;
}

/* Content styles */
.content {
  margin-left: 250px;
  padding: 20px;
}
```

### Explanation:

1. **Sidebar Styling**:
   - The `.sidebar` is fixed to the left side of the page and has a width of `250px`. It spans the entire height of the window.
   - Links inside the sidebar have padding, are block elements, and change color when hovered over.

2. **Dropdown Menu**:
   - The `.dropdown-content` is hidden by default using `display: none;`.
   - When the user hovers over the `.dropdown`, the `dropdown-content` becomes visible with `display: block;`.
   - The submenu links have smaller padding and a slightly different background color when hovered over.

3. **Main Menu with Dropdown**:
   - The `.main-menu` links are clickable and contain an arrow (`▼`) after the text, which indicates the presence of a submenu. This is done using the `::after` pseudo-element.
   - Submenus only appear on hover, but the main menu links remain clickable.

---

## Final Thoughts

This example shows how you can create a sidebar navigation with main menu items that have links and expandable submenus. The design is flexible and can be enhanced further with animations, icons, or more advanced features.
