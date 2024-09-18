
# HTML and CSS Media Query Tutorial (Without Flexbox)

Media queries are used to apply styles based on the device's properties, like screen size or orientation. This tutorial will help you understand how to create responsive designs using media queries without relying on Flexbox.

## 1. Basic Media Query Syntax

The basic syntax for a media query:

```css
@media (condition) {
  /* CSS rules go here */
}
```

Example:

```css
/* Default styles */
body {
  background-color: lightblue;
}

/* Styles for screens larger than 600px */
@media (min-width: 600px) {
  body {
    background-color: lightgreen;
  }
}

/* Styles for screens smaller than 600px */
@media (max-width: 600px) {
  body {
    background-color: lightcoral;
  }
}
```

## 2. Using Media Queries for Responsive Design

Responsive design allows the layout to change based on the screen size. Here’s how to use simple CSS properties to adjust elements:

```css
/* Default styles for mobile (small screens) */
.container {
  width: 100%;
  padding: 10px;
}

/* Tablet view (medium screens) */
@media (min-width: 768px) {
  .container {
    width: 80%;
    margin: 0 auto; /* Centers the container */
    padding: 20px;
  }
}

/* Desktop view (large screens) */
@media (min-width: 1024px) {
  .container {
    width: 60%;
    margin: 0 auto;
    padding: 30px;
  }
}
```

## 3. Building a Responsive Navigation Bar Without Flexbox

Here’s how to create a responsive navigation bar using basic CSS properties:

### HTML
```html
<nav class="navbar">
  <ul class="nav-links">
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Services</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

### CSS
```css
/* Basic styles for navbar */
.navbar {
  background-color: #333;
  overflow: hidden; /* Ensures proper layout */
}

.nav-links {
  list-style-type: none;
  margin: 0;
  padding: 0;
  text-align: center; /* Centers text */
}

.nav-links li {
  display: inline-block; /* Places links horizontally */
}

.nav-links li a {
  color: white;
  text-decoration: none;
  padding: 14px 20px;
  display: block;
}

/* Media query for screens smaller than 600px */
@media (max-width: 600px) {
  .nav-links li {
    display: block; /* Stacks links vertically */
  }

  .nav-links {
    text-align: left; /* Align text to the left */
  }
}
```

In this example:
- For screens larger than 600px, the navigation links are displayed horizontally using `display: inline-block`.
- For smaller screens, the media query changes the links to stack vertically by setting `display: block`.

## 4. Simple Grid Layout Without Flexbox

You can create a responsive grid using basic CSS properties. Here's how:

### HTML
```html
<div class="grid-container">
  <div class="grid-item">Item 1</div>
  <div class="grid-item">Item 2</div>
  <div class="grid-item">Item 3</div>
</div>
```

### CSS
```css
/* Default styles for mobile (single column) */
.grid-container {
  width: 100%;
}

.grid-item {
  width: 100%;
  padding: 10px;
  box-sizing: border-box; /* Includes padding in width */
  border: 1px solid #ccc;
}

/* Tablet view (two columns) */
@media (min-width: 600px) {
  .grid-item {
    width: 49%; /* Two columns with a small gap */
    float: left; /* Floats items to the left */
  }
}

/* Desktop view (three columns) */
@media (min-width: 900px) {
  .grid-item {
    width: 32%; /* Three columns with some spacing */
    float: left;
  }
}
```

In this example:
- On small screens (mobile), each `.grid-item` takes up 100% of the width.
- On medium screens (tablets), the items use `float: left` to create a two-column layout.
- On larger screens (desktops), it shifts to a three-column layout.

## 5. Orientation-Based Media Queries

You can use media queries to apply styles based on the screen orientation:

```css
/* Styles for portrait orientation */
@media (orientation: portrait) {
  body {
    background-color: lavender;
  }
}

/* Styles for landscape orientation */
@media (orientation: landscape) {
  body {
    background-color: peachpuff;
  }
}
```

## 6. Combining Media Queries

You can combine multiple conditions in a media query using `and`, `not`, and `only`:

```css
/* Target screens between 600px and 900px in width */
@media (min-width: 600px) and (max-width: 900px) {
  .sidebar {
    display: none;
  }
}
```

## 7. Testing Media Queries

You can test media queries by resizing the browser window or using the developer tools in your browser (F12) to simulate different screen sizes and orientations.

## Conclusion

Media queries are essential for creating responsive websites. By adjusting styles based on screen size or orientation, you can build a user-friendly interface that works across various devices without needing complex layout techniques like Flexbox. This tutorial focused on basic CSS properties like `width`, `float`, and `display` to help you get started.
