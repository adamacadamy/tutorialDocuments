
# Simple Navigation Bar Tutorial

## Step 1: Basic HTML Structure
Start by creating the basic HTML structure with a navigation section.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simple Navbar</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <nav>
    <ul>
      <li><a href="#home">Home</a></li>
      <li><a href="#about">About</a></li>
      <li><a href="#services">Services</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>

</body>
</html>
```

## Step 2: CSS for Styling the Navbar
Now, add some CSS to style the navbar. Create a `styles.css` file and link it to your HTML.

```css
/* Reset some default styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Basic styles for the body */
body {
  font-family: Arial, sans-serif;
}

/* Styling the navigation bar */
nav {
  background-color: #333; /* Dark background color */
  padding: 10px;
}

/* Styling the list items */
nav ul {
  list-style-type: none;
  display: flex;
  justify-content: center; /* Center the nav items */
}

/* Styling each nav item */
nav ul li {
  margin: 0 15px;
}

/* Styling the links */
nav ul li a {
  color: white;
  text-decoration: none;
  font-size: 18px;
  padding: 10px 20px;
  display: block;
  transition: background-color 0.3s ease;
}

/* Hover effect for links */
nav ul li a:hover {
  background-color: #555;
  border-radius: 5px;
}
```

## Explanation:
1. **HTML:**
   - The `<nav>` tag holds the navigation bar.
   - An unordered list (`<ul>`) contains list items (`<li>`) for each link.
   - Each list item has an anchor tag (`<a>`) that links to different sections of the page.

2. **CSS:**
   - We set a background color and padding for the `<nav>` to make it stand out.
   - The `ul` is set to display its items in a row using `display: flex`.
   - The anchor tags are styled to look clean, with padding for spacing and a hover effect for interactivity.

## Result:
This creates a centered navigation bar with four links: Home, About, Services, and Contact. When you hover over a link, the background color changes.

Feel free to modify the colors, font sizes, or layout to match your design preferences!
