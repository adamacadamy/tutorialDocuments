
# Flexbox Grid Layout & Menu Bar Solution

## Task 1: Responsive Menu Bar

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Responsive Menu Bar</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #333;
            padding: 1em;
            color: white;
        }
        .navbar .logo {
            font-size: 1.5em;
            font-weight: bold;
        }
        .navbar .nav-links {
            display: flex;
            list-style: none;
        }
        .navbar .nav-links li {
            margin-left: 1em;
        }
        .navbar .nav-links a {
            text-decoration: none;
            color: white;
            padding: 0.5em;
        }
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                align-items: flex-start;
            }
            .navbar .nav-links {
                flex-direction: column;
                width: 100%;
            }
            .navbar .nav-links li {
                margin: 0.5em 0;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="logo">LOGO</div>
        <ul class="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
</body>
</html>
```

## Task 2: Responsive Flexbox Grid Layout

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Responsive Flexbox Grid Layout</title>
    <style>
        .grid-container {
            display: flex;
            flex-wrap: wrap;
            gap: 1em;
            padding: 1em;
        }
        .grid-item {
            flex: 1 1 calc(33.333% - 1em);
            background-color: #4CAF50;
            color: white;
            padding: 2em;
            text-align: center;
            font-size: 1.5em;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        @media (max-width: 768px) {
            .grid-item {
                flex: 1 1 calc(50% - 1em);
            }
        }
        @media (max-width: 480px) {
            .grid-item {
                flex: 1 1 100%;
            }
        }
    </style>
</head>
<body>
    <div class="grid-container">
        <div class="grid-item">1</div>
        <div class="grid-item">2</div>
        <div class="grid-item">3</div>
        <div class="grid-item">4</div>
        <div class="grid-item">5</div>
        <div class="grid-item">6</div>
    </div>
</body>
</html>
```

## Explanation:

- **Navigation Bar**:
  - On large screens, the navigation bar shows the logo on the left and links aligned to the right.
  - On small screens, the layout is adjusted using media queries to stack the links vertically.
  
- **Flexbox Grid Layout**:
  - On large screens, the items are arranged in three columns.
  - On medium screens, the layout changes to two columns, and on small screens, items are stacked in a single column.
  
These solutions ensure the layout is responsive without the use of JavaScript, leveraging Flexbox and media queries for adjustments.