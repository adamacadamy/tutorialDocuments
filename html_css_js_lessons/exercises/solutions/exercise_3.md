
# Inline-Block Gallery Solution

## Solution Description
This solution demonstrates how to create an inline-block image gallery using `div` tags styled with CSS. The solution includes spacing, borders, hover effects, and ensures that images scale correctly within their containers.

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
        <div class="image-container"><img src="images/image1.jpg" alt="Image 1"></div>
        <div class="image-container"><img src="images/image2.jpg" alt="Image 2"></div>
        <div class="image-container"><img src="images/image3.jpg" alt="Image 3"></div>
        <div class="image-container"><img src="images/image4.jpg" alt="Image 4"></div>
        <div class="image-container"><img src="images/image5.jpg" alt="Image 5"></div>
        <div class="image-container"><img src="images/image6.jpg" alt="Image 6"></div>
        <div class="image-container"><img src="images/image7.jpg" alt="Image 7"></div>
        <div class="image-container"><img src="images/image8.jpg" alt="Image 8"></div>
        <div class="image-container"><img src="images/image9.jpg" alt="Image 9"></div>
        <div class="image-container"><img src="images/image10.jpg" alt="Image 10"></div>
    </div>
</body>
</html>
```

### 2. **CSS File (`styles.css`)**

Create a `styles.css` file with the following content:

```css
/* Basic styles for the gallery */
.gallery {
    text-align: center; /* Center the gallery */
}

/* Styling for the image containers */
.image-container {
    display: inline-block;
    width: 200px; /* Set a fixed width for the image containers */
    margin: 10px; /* Spacing around each image container */
    padding: 10px; /* Padding inside each container */
    background-color: #fff; /* Light background color */
    border: 1px solid #ccc; /* Border around each container */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle box shadow */
    transition: transform 0.3s ease, box-shadow 0.3s ease; /* Transition for hover effects */
}

/* Ensure images fit within the container */
.image-container img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
}

/* Hover effect for scaling the container */
.image-container:hover {
    transform: scale(1.1); /* Scale up the container */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Increase shadow on hover */
}

/* Extra: Remove white space between inline-block elements */
.gallery {
    font-size: 0; /* Remove white space by setting font-size to 0 */
}

.image-container {
    font-size: 16px; /* Reset font size for content inside containers */
}
```

### Explanation

1. **HTML Structure:**
    - The HTML file contains a parent `div` with the class `gallery`.
    - Inside the `gallery`, there are 10 child `div` elements, each with the class `image-container`, containing an `img` tag for the images.

2. **CSS Styling:**
    - **`.gallery` class:** Centers the entire gallery and addresses the white space issue between inline-block elements by setting `font-size: 0;`.
    - **`.image-container` class:**
        - Uses `display: inline-block` to arrange the containers next to each other.
        - Sets a fixed width and adds padding, margin, background color, and border for visual structure.
        - Applies a box shadow to give a subtle 3D effect.
        - Uses the `transition` property for smooth hover effects.
    - **`.image-container img` style:** Ensures the images fit within their containers without exceeding the set boundaries.
    - **Hover Effect:** The `:hover` pseudo-class applies scaling (`transform: scale(1.1)`) and increases the shadow for a more pronounced effect on hover.
    - **Extra:** Removes white space between inline-block elements by setting the `font-size` of `.gallery` to `0`.

### 3. **Bonus: Making Images Responsive**

To make the images responsive and ensure they resize automatically when the window is resized, the `max-width: 100%;` and `height: auto;` properties on the `img` tag handle the resizing based on the container's width.

### 4. **Optional Challenge Solution:**
- The white space between `inline-block` elements is handled by setting the `font-size` of the parent container (`.gallery`) to `0`.

This solution creates a responsive inline-block image gallery using `div` tags, including spacing, borders, and hover effects without using JavaScript.
