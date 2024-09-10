
# Styled Div Examples

## HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Styled Div Examples</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Box Model Example -->
  <div class="box-model">
    This is a box model example.
  </div>

  <!-- Background Example -->
  <div class="background">
    Background example
  </div>

  <!-- Text Styling Example -->
  <div class="text-styling">
    Styled text inside a div
  </div>

  <!-- Display and Layout Example -->
  <div class="inline-box">Inline-block example</div>
  <div class="inline-box">Next to it</div>

  <div class="positioned-box">
    Positioned absolutely
  </div>

  <!-- Flexbox Layout Example -->
  <div class="flexbox-container">
    <div>Item 1</div>
    <div>Item 2</div>
    <div>Item 3</div>
  </div>

  <!-- Grid Layout Example -->
  <div class="grid-container">
    <div>Grid Item 1</div>
    <div>Grid Item 2</div>
    <div>Grid Item 3</div>
  </div>

  <!-- Visibility and Overflow Example -->
  <div class="hidden-box">
    This text is hidden
  </div>

  <div class="overflow-box">
    Content that overflows the box will have a scrollbar. Content that overflows the box will have a scrollbar.
  </div>

  <!-- Box Shadow Example -->
  <div class="shadow-box">
    Box with shadow
  </div>

  <!-- Border Radius Example -->
  <div class="rounded-box">
    Rounded corners
  </div>

  <!-- Transition and Animation Example -->
  <div class="transition-box">
    Hover over me
  </div>

  <div class="animated-box">
    Animated box
  </div>
</body>
</html>
```

## CSS

```css
/* Box Model Example */
.box-model {
  width: 200px;
  height: 100px;
  padding: 10px;
  margin: 20px;
  border: 1px solid black;
}

/* Background Example */
.background {
  width: 300px;
  height: 200px;
  background-color: #f0f0f0;
  background-image: url('image.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

/* Text Styling Example */
.text-styling {
  color: #333;
  font-size: 18px;
  font-family: Arial, sans-serif;
  text-align: center;
}

/* Display and Layout Example */
.inline-box {
  display: inline-block;
  width: 100px;
  height: 100px;
  background-color: lightblue;
}

.positioned-box {
  position: absolute;
  top: 50px;
  left: 100px;
  width: 200px;
  height: 100px;
  background-color: yellow;
}

/* Flexbox Layout Example */
.flexbox-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100px;
  background-color: lightgray;
}

/* Grid Layout Example */
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 10px;
}

.grid-container div {
  background-color: lightblue;
}

/* Visibility and Overflow Example */
.hidden-box {
  visibility: hidden;
}

.overflow-box {
  width: 100px;
  height: 100px;
  background-color: lightblue;
  overflow: auto;
}

/* Box Shadow Example */
.shadow-box {
  width: 200px;
  height: 100px;
  background-color: white;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
}

/* Border Radius Example */
.rounded-box {
  width: 100px;
  height: 100px;
  background-color: lightblue;
  border-radius: 50px;
}

/* Transition and Animation Example */
.transition-box {
  width: 100px;
  height: 100px;
  background-color: lightblue;
  transition: background-color 0.5s;
}

.transition-box:hover {
  background-color: lightcoral;
}

/* Animation Example */
.animated-box {
  width: 100px;
  height: 100px;
  background-color: lightblue;
  animation: slide-in 2s ease;
}

@keyframes slide-in {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}
```

### Instructions

1. Save the HTML code in one file (e.g., `index.html`).
2. Save the CSS code in another file (e.g., `styles.css`).
3. Link the `styles.css` in your HTML using the `<link>` tag, as shown in the HTML code.
4. Open `index.html` in your browser to see the styled div examples in action.



# Styling Unordered (`<ul>`) and Ordered (`<ol>`) Lists in HTML

This file demonstrates how to apply custom styles to both `<ul>` (unordered lists) and `<ol>` (ordered lists) elements using CSS.

## HTML Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styled Lists</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <h1>Styled Unordered List</h1>
    <ul>
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    </ul>

    <h1>Styled Ordered List</h1>
    <ol>
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    </ol>

</body>
</html>
```

## CSS Example

```css
ul, ol {
    list-style-type: none; /* Removes bullet points or numbers */
    padding: 0; /* Removes default padding */
    margin: 0; /* Removes default margin */
    font-family: Arial, sans-serif; /* Sets the font */
    font-size: 16px; /* Sets the font size */
    color: #333; /* Sets the text color */
}

ul li, ol li {
    padding: 10px; /* Adds padding to each list item */
    border-bottom: 1px solid #ccc; /* Adds a border below each item */
}

ul li:last-child, ol li:last-child {
    border-bottom: none; /* Removes border from the last item */
}
```

## Notes

- Both the `<ul>` and `<ol>` elements share the same styles.
- The `list-style-type` property removes the default bullets or numbering.
- Padding and margin are reset to provide custom spacing.
- Text styling is applied via `font-family`, `font-size`, and `color`.
- List items have borders between them, except for the last item.

Simply copy the HTML and CSS code into separate `.html` and `.css` files to see the results in a browser.



# Image Tag CSS Styles

The `<img>` tag in HTML is used to embed images. Below is a comprehensive list of CSS styles you can apply to the `<img>` tag for customization.

## Basic Styles

### Width & Height
```css
width: 200px;
height: 150px;
```

### Border
```css
border: 2px solid black;
border-radius: 8px; /* To make the edges rounded */
```

### Padding
```css
padding: 10px;
```

### Margin
```css
margin: 15px;
```

### Box Shadow
```css
box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.5);
```

### Opacity
```css
opacity: 0.8;
```

### Object Fit
```css
object-fit: cover;  /* Possible values: fill, contain, cover, scale-down */
```

### Float
```css
float: left;
```

### Display
```css
display: block;
```

### Positioning
```css
position: relative;
top: 10px;
left: 20px;
```

## Advanced Styles

### Filter Effects
#### Grayscale
```css
filter: grayscale(100%);
```

#### Blur
```css
filter: blur(5px);
```

#### Sepia
```css
filter: sepia(100%);
```

### Hover Effects
#### Zoom on hover
```css
img:hover {
  transform: scale(1.2);
  transition: 0.3s;
}
```

### Image Alignment
Align the image in relation to text:
```css
vertical-align: middle; /* Possible values: top, bottom, text-top */
```

### Animation
```css
img {
  animation: rotateImage 5s infinite;
}

@keyframes rotateImage {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

### CSS Masking
```css
mask-image: linear-gradient(to bottom, transparent, black);
```

### Responsive Images
```css
max-width: 100%;
height: auto;
```

### Aspect Ratio
```css
aspect-ratio: 16/9;
```

These styles allow you to customize images on your webpage efficiently.



# CSS Styles for `<p>` Element

## Basic Text Styling

1. **Font Family**:
    ```css
    p {
      font-family: Arial, sans-serif;
    }
    ```

2. **Font Size**:
    ```css
    p {
      font-size: 16px;
    }
    ```

3. **Font Weight**:
    ```css
    p {
      font-weight: bold;
    }
    ```

4. **Font Style**:
    ```css
    p {
      font-style: italic;
    }
    ```

5. **Text Color**:
    ```css
    p {
      color: #333;
    }
    ```

6. **Text Alignment**:
    ```css
    p {
      text-align: center;
    }
    ```

7. **Text Decoration**:
    ```css
    p {
      text-decoration: underline;
    }
    ```

8. **Text Transform**:
    ```css
    p {
      text-transform: uppercase;
    }
    ```

9. **Letter Spacing**:
    ```css
    p {
      letter-spacing: 2px;
    }
    ```

10. **Line Height**:
    ```css
    p {
      line-height: 1.5;
    }
    ```

## Box Model Properties

1. **Margin**:
    ```css
    p {
      margin: 20px 0;
    }
    ```

2. **Padding**:
    ```css
    p {
      padding: 10px;
    }
    ```

3. **Border**:
    ```css
    p {
      border: 1px solid #ccc;
    }
    ```

4. **Background Color**:
    ```css
    p {
      background-color: #f0f0f0;
    }
    ```

## Advanced Styling

1. **Text Shadow**:
    ```css
    p {
      text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    ```

2. **Word Spacing**:
    ```css
    p {
      word-spacing: 5px;
    }
    ```

3. **Overflow (for long text)**:
    ```css
    p {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    ```

4. **First Letter/Line Styling**:
    ```css
    p::first-letter {
      font-size: 2em;
      color: red;
    }
    ```

5. **Opacity**:
    ```css
    p {
      opacity: 0.8;
    }
    ```

6. **Visibility**:
    ```css
    p {
      visibility: hidden;
    }
    ```

7. **Box Shadow**:
    ```css
    p {
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    ```

---

Feel free to customize these CSS properties as needed in your project!
