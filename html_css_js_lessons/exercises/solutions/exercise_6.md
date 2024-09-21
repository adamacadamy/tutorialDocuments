
# Media Query Code Challenge Solutions

Below are the solutions to the media query code challenges.

## Code Challenge 1: Basic Media Query Implementation

### HTML
```html
<div class="color-box">
  This is a color-changing box!
</div>
```

### CSS
```css
/* Default styles */
.color-box {
  background-color: lightblue;
  padding: 20px;
  text-align: center;
}

/* Styles for screens larger than 768px */
@media (min-width: 768px) {
  .color-box {
    background-color: lightgreen;
  }
}

/* Styles for screens smaller than 480px */
@media (max-width: 480px) {
  .color-box {
    background-color: lightcoral;
  }
}

/* Bonus: Change color based on orientation */
@media (orientation: portrait) {
  .color-box {
    background-color: lavender;
  }
}
```

## Code Challenge 2: Responsive Navigation Bar Without Flexbox

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
  overflow: hidden;
}

.nav-links {
  list-style-type: none;
  margin: 0;
  padding: 0;
  text-align: center;
}

.nav-links li {
  display: inline-block;
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
    display: block;
  }

  .nav-links {
    text-align: left;
  }

  /* Bonus: Change text color in vertical mode */
  .nav-links li a {
    color: lightblue;
  }
}
```

## Code Challenge 3: Responsive Grid Layout Without Flexbox

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
  box-sizing: border-box;
  border: 1px solid #ccc;
}

/* Tablet view (two columns) */
@media (min-width: 600px) {
  .grid-item {
    width: 49%;
    float: left;
  }
}

/* Desktop view (three columns) */
@media (min-width: 900px) {
  .grid-item {
    width: 32%;
    float: left;
  }
}

/* Bonus: Hover effect */
.grid-item:hover {
  background-color: lightgray;
}
```

## Code Challenge 4: Image Gallery with Responsive Columns

### HTML
```html
<div class="image-gallery">
  <img src="image1.jpg" alt="Image 1">
  <img src="image2.jpg" alt="Image 2">
  <img src="image3.jpg" alt="Image 3">
  <img src="image4.jpg" alt="Image 4">
  <img src="image5.jpg" alt="Image 5">
  <img src="image6.jpg" alt="Image 6">
</div>
```

### CSS
```css
/* Default styles for mobile (single column) */
.image-gallery img {
  width: 100%;
  padding: 5px;
  box-sizing: border-box;
}

/* Tablet view (two columns) */
@media (min-width: 500px) and (max-width: 800px) {
  .image-gallery img {
    width: 49%;
  }
}

/* Desktop view (four columns) */
@media (min-width: 800px) {
  .image-gallery img {
    width: 24%;
  }
}

/* Bonus: Add padding */
.image-gallery img {
  padding: 10px;
}
```

## Code Challenge 5: Responsive Card Layout

### HTML
```html
<div class="card-container">
  <div class="card">
    <img src="card-image1.jpg" alt="Image 1">
    <h3>Title 1</h3>
    <p>Description for card 1.</p>
  </div>
  <div class="card">
    <img src="card-image2.jpg" alt="Image 2">
    <h3>Title 2</h3>
    <p>Description for card 2.</p>
  </div>
  <div class="card">
    <img src="card-image3.jpg" alt="Image 3">
    <h3>Title 3</h3>
    <p>Description for card 3.</p>
  </div>
  <div class="card">
    <img src="card-image4.jpg" alt="Image 4">
    <h3>Title 4</h3>
    <p>Description for card 4.</p>
  </div>
</div>
```

### CSS
```css
/* Default styles for mobile (single column) */
.card-container {
  width: 100%;
}

.card {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
  border: 1px solid #ccc;
}

/* Tablet view (two columns) */
@media (min-width: 600px) and (max-width: 900px) {
  .card {
    width: 49%;
    float: left;
  }
}

/* Desktop view (three columns) */
@media (min-width: 900px) {
  .card {
    width: 32%;
    float: left;
  }
}

/* Bonus: Change card background color on hover */
.card:hover {
  background-color: lightgray;
}
```

## Code Challenge 6: Adjust Text Size Using Media Queries

### HTML
```html
<div class="text-container">
  <h1>Responsive Heading</h1>
  <p>This is a paragraph that changes size based on screen width.</p>
</div>
```

### CSS
```css
/* Default font sizes */
.text-container h1 {
  font-size: 24px;
}

.text-container p {
  font-size: 16px;
}

/* Increase font size for screens larger than 800px */
@media (min-width: 800px) {
  .text-container h1 {
    font-size: 32px;
  }

  .text-container p {
    font-size: 20px;
  }
}

/* Decrease font size for screens smaller than 500px */
@media (max-width: 500px) {
  .text-container h1 {
    font-size: 18px;
  }

  .text-container p {
    font-size: 14px;
  }
}

/* Bonus: Change font style in portrait orientation */
@media (orientation: portrait) {
  .text-container p {
    font-style: italic;
  }
}
```

---

These solutions demonstrate how to implement responsive designs using media queries without relying on Flexbox.
