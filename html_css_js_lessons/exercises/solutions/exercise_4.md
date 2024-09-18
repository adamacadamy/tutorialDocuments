
# Inline-Block Gallery Solution with `info-container` Class

## Solution Description
This solution involves creating a gallery using `info-container` elements that each contain an image and some text. We use the `float: left` property to arrange the elements side-by-side and provide visual styling, spacing, and hover effects with CSS.

### 1. **HTML File (`index.html`)**

Create an `index.html` file with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inline-Block Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="gallery">
        <div class="info-container">
            <div class="image-container">
                <img src="images/image1.jpg" alt="Image 1">
            </div>
            <div class="text-container">
                <p>Some text information here.</p>
            </div>
        </div>
        <!-- Repeat the above block for 9 more items -->
        <div class="info-container">
            <div class="image-container">
                <img src="images/image2.jpg" alt="Image 2">
            </div>
            <div class="text-container">
                <p>Additional text information here.</p>
            </div>
        </div>
        <!-- Add more info-container blocks as needed -->
    </div>
</body>
</html>
```

### 2. **CSS File (`styles.css`)**

Create a `styles.css` file with the following content:

```css
/* Basic styles for the gallery */
.gallery {
    width: 100%;
    overflow: hidden; /* Clear floats */
}

/* Styling for each info-container */
.info-container {
    float: left;
    width: 30%; /* Set a fixed width for each container */
    margin: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    background-color: #f9f9f9;
    box-sizing: border-box; /* Include padding and border in the width */
    transition: transform 0.3s ease; /* Transition for hover effect */
}

/* Image container styles */
.image-container {
    width: 100%;
}

/* Text container styles */
.text-container {
    width: 100%;
    margin-top: 10px;
}

/* Image styling */
.info-container img {
    width: 100%;
    height: auto;
}

/* Hover effect for scaling the image */
.info-container:hover img {
    transform: scale(1.1);
}

/* Clear floats to ensure containers wrap correctly */
.gallery::after {
    content: "";
    display: table;
    clear: both;
}
```

### Explanation

1. **HTML Structure:**
    - The HTML file contains a parent `div` with the class `gallery`.
    - Each `info-container` has two child `div` elements:
        - `image-container` for the image.
        - `text-container` for the text information.

2. **CSS Styling:**
    - **`.gallery` class:** Uses `overflow: hidden;` to clear the floats and ensure proper wrapping of `info-container` elements.
    - **`.info-container` class:**
        - Uses `float: left;` to arrange the elements side-by-side.
        - Sets a fixed width (`30%`), margin, padding, border, and background color for visual separation.
        - Applies `box-sizing: border-box;` to include padding and border in the total width.
    - **`.image-container` and `.text-container`:** Ensures the image and text take up the full width of the `info-container`.
    - **`.info-container img` style:** Ensures images fit within their containers, maintaining their aspect ratio.
    - **Hover Effect:** The `:hover` pseudo-class scales up the image inside the `info-container` using `transform: scale(1.1);`.
    - **Clearing Floats:** The `.gallery::after` selector ensures that the floating containers wrap correctly by using the clearfix method.

This solution satisfies the exercise's requirements by using `float: left` to arrange elements, adding spacing, borders, background color, and implementing a hover effect to scale images.
