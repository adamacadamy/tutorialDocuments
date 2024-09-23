
# CSS Box Model Challenge Solution

## Solution Description
This solution demonstrates the use of the CSS box model to style elements using padding, margins, borders, and width/height properties. It also includes additional styling for centering the boxes and adding background colors.

### 1. **HTML File (`index.html`)**

Create an `index.html` file with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Box Model Challenge</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="box box1">Box 1</div>
    <div class="box box2">Box 2</div>
    <div class="box box3">Box 3</div>
</body>
</html>
```

### 2. **CSS File (`styles.css`)**

Create a `styles.css` file with the following content to style the boxes according to the instructions:

```css
/* Basic styling for the body */
body {
    display: flex;
    flex-direction: column;
    align-items: center; /* Centers the boxes horizontally */
    justify-content: center;
    min-height: 100vh;
    margin: 0;
    background-color: #f0f0f0;
}

/* Common styles for all boxes */
.box {
    width: 200px;
    height: 100px;
    padding: 15px;
    margin: 10px;
    color: white;
    text-align: center;
    line-height: 70px; /* Centers text vertically within the box */
}

/* Specific styles for each box */
.box1 {
    border: 3px solid red;
    background-color: #ff6666;
}

.box2 {
    border: 3px solid blue;
    background-color: #6666ff;
}

.box3 {
    border: 3px solid green;
    background-color: #66cc66;
}
```

### Explanation

1. **HTML File:** The HTML file includes three `div` elements with the class `box` and unique classes (`box1`, `box2`, `box3`) for specific styling.

2. **CSS File:** 
    - The `.box` class defines common box properties:
        - `width`: 200px
        - `height`: 100px
        - `padding`: 15px
        - `margin`: 10px
    - Each specific box class (`.box1`, `.box2`, `.box3`) has its own border color and background color.
    - The `body` is styled with `display: flex` and `align-items: center` to center the boxes horizontally in the browser window.
    - `line-height` is used to vertically center the text inside each box.

This solution satisfies the challenge's requirements by applying box model properties and styling each box according to the instructions. The bonus tasks of centering the boxes and adding background colors have also been completed.
