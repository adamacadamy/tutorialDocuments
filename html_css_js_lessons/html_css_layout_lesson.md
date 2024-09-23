
# HTML and CSS Layouts - Basic Techniques and Holy Grail Layout

## Introduction
This guide covers various basic layout techniques in HTML and CSS, without using Flexbox. It includes:
1. Block-level elements for default vertical stacking.
2. Floats for multi-column layouts.
3. Inline-block for side-by-side alignment.
4. Positioning for advanced control.
5. The "Holy Grail" layout combining all these techniques.

## Basic Layouts

### 1. Block Elements (Default Flow)
By default, HTML block-level elements like `div`, `header`, `footer`, stack one on top of the other.

**HTML:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Layout</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>Header</header>
    <nav>Navigation</nav>
    <main>Main Content</main>
    <aside>Sidebar</aside>
    <footer>Footer</footer>
</body>
</html>
```

**CSS:**
```css
/* Basic styles for elements */
header, nav, main, aside, footer {
    padding: 20px;
    margin: 10px;
    background-color: lightgray;
}
```

### 2. Using `float` Property
The `float` property can create columns.

**HTML:**
```html
<div class="container">
    <header>Header</header>
    <div class="content">
        <nav>Navigation</nav>
        <main>Main Content</main>
    </div>
    <footer>Footer</footer>
</div>
```

**CSS:**
```css
/* Container for layout */
.container {
    width: 100%;
}

/* Clear floats */
.content::after {
    content: "";
    display: table;
    clear: both;
}

/* Float the nav to create a sidebar */
nav {
    float: left;
    width: 25%;
    background-color: lightblue;
}

/* Main content */
main {
    float: left;
    width: 75%;
    background-color: lightgreen;
}

/* Header and footer */
header, footer {
    clear: both;
    background-color: lightgray;
    text-align: center;
    padding: 20px;
}
```

### 3. Using `inline-block`
Using `inline-block` allows elements to be placed side by side.

**HTML:**
```html
<div class="container">
    <header>Header</header>
    <div class="content">
        <nav>Navigation</nav>
        <main>Main Content</main>
    </div>
    <footer>Footer</footer>
</div>
```

**CSS:**
```css
/* Setting inline-block */
nav, main {
    display: inline-block;
    vertical-align: top;
}

/* Set widths */
nav {
    width: 25%;
    background-color: lightblue;
}

main {
    width: 70%; /* Less than 75% to account for margin or padding */
    background-color: lightgreen;
}

/* Header and footer */
header, footer {
    background-color: lightgray;
    text-align: center;
    padding: 20px;
}

/* Clear the content section */
.content {
    white-space: nowrap; /* Prevent line breaks */
}
```

### 4. Using `position` Property
The `position` property can be used to create fixed, absolute, or relative layouts.

**HTML:**
```html
<div class="container">
    <header>Header</header>
    <nav>Navigation</nav>
    <main>Main Content</main>
    <footer>Footer</footer>
</div>
```

**CSS:**
```css
/* Basic layout */
.container {
    position: relative;
}

/* Fixed header */
header {
    position: fixed;
    top: 0;
    width: 100%;
    background-color: lightgray;
    padding: 20px;
    text-align: center;
}

/* Navigation and main content */
nav {
    position: absolute;
    top: 80px; /* Offset below the fixed header */
    left: 0;
    width: 20%;
    background-color: lightblue;
    height: 100vh; /* Full viewport height */
}

main {
    margin-left: 20%;
    margin-top: 80px; /* Offset below the fixed header */
    background-color: lightgreen;
    padding: 20px;
}

/* Footer */
footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    background-color: lightgray;
    text-align: center;
    padding: 20px;
}
```

## The Holy Grail Layout
Combines all the techniques discussed.

**HTML:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Holy Grail Layout</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>Header</header>
        <nav>Navigation</nav>
        <div class="content">
            <aside class="left-sidebar">Left Sidebar</aside>
            <main>Main Content</main>
            <aside class="right-sidebar">Right Sidebar</aside>
        </div>
        <footer>Footer</footer>
    </div>
</body>
</html>
```

**CSS:**
```css
/* Basic Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Container to center content */
.container {
    width: 100%;
    min-height: 100vh;
    position: relative;
}

/* Header and Footer */
header, footer {
    background-color: lightgray;
    text-align: center;
    padding: 20px;
    width: 100%;
}

/* Navigation Bar */
nav {
    background-color: lightblue;
    padding: 10px;
    text-align: center;
}

/* Main content wrapper */
.content {
    overflow: hidden; /* Clear floats */
    padding: 10px;
}

/* Left Sidebar */
.left-sidebar {
    float: left;
    width: 20%;
    background-color: lightcoral;
    padding: 10px;
}

/* Right Sidebar */
.right-sidebar {
    float: right;
    width: 20%;
    background-color: lightgreen;
    padding: 10px;
}

/* Main Content */
main {
    margin: 0 20%;
    background-color: lightyellow;
    padding: 10px;
}

/* Footer Fix */
footer {
    clear: both;
}

/* Positioning Examples */
nav {
    position: sticky;
    top: 0;
    z-index: 10;
}

/* Clearfix to ensure proper layout */
.content::after {
    content: "";
    display: table;
    clear: both;
}

/* Media Query for Responsiveness */
@media (max-width: 768px) {
    .left-sidebar, .right-sidebar {
        float: none;
        width: 100%;
        display: block;
    }

    main {
        margin: 0;
    }
}
```
