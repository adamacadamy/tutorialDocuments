
# Flexbox Grid Layout Lesson

In this lesson, we will use Flexbox to create a grid-like layout that automatically adjusts based on the screen size.

## Step 1: HTML Structure

We will create a basic structure where we have a container, and inside it, we will place grid items.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flexbox Grid Layout</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <div class="container">
        <div class="box">1</div>
        <div class="box">2</div>
        <div class="box">3</div>
        <div class="box">4</div>
        <div class="box">5</div>
        <div class="box">6</div>
    </div>

</body>
</html>
```

## Step 2: Styling the Flexbox Grid (CSS)

Now, we will style the container to use Flexbox and control the grid layout using flex properties.

```css
/* General reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f4f4f4;
}

/* Flexbox container */
.container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    width: 80%;
    max-width: 1200px;
}

/* Individual grid items */
.box {
    background-color: #3498db;
    color: white;
    padding: 20px;
    flex: 1 1 calc(33.333% - 10px);
    margin: 5px;
    text-align: center;
    font-size: 1.5rem;
}

/* Responsive Design for smaller screens */
@media (max-width: 768px) {
    .box {
        flex: 1 1 calc(50% - 10px);
    }
}

@media (max-width: 480px) {
    .box {
        flex: 1 1 100%;
    }
}
```

## Step 3: Explanation of Flexbox Properties

- **Container Styles (`.container`):**
  - `display: flex;`: This makes the container a Flexbox container.
  - `flex-wrap: wrap;`: This ensures that the items wrap onto the next line when there isn't enough space.
  - `justify-content: space-between;`: This adds space between the grid items.

- **Item Styles (`.box`):**
  - `flex: 1 1 calc(33.333% - 10px);`: Each box takes up 1/3 of the container width, minus the margin.
  - The boxes will adjust and fill up the available space evenly.

## Step 4: Making It Responsive

- **Responsive Design:**
  - When the screen width is less than 768px, the boxes will adjust to be 50% of the container width.
  - When the screen width is less than 480px, each box will take up the full width of the container.

## Step 5: Testing the Grid Layout

- Open this code in a browser, and resize the window to see how the grid layout adapts to different screen sizes.

---

This example shows how you can create a grid-like layout with Flexbox while keeping it responsive across different screen sizes.
