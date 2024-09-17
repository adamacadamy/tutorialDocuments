
# Inline-Block Gallery with `info-container` Class Exercise

**Objective:**  
Create an inline-block gallery with 10 `info-container` elements. Each element should contain two `div` tags inside:
1. One `div` containing an image.
2. Another `div` containing text information.

Apply CSS to style the layout so that each `info-container` uses the `float: left` property.

---

## Instructions

1. **HTML Structure:**
   - Create an HTML page with 10 `info-container` elements.
   - Each `info-container` should have the class `info-container`.
   - Inside each `info-container`, there should be two `div` tags:
     - The first `div` containing an image.
     - The second `div` containing some text information.

2. **Floating Layout:**
   - Using CSS, apply the `float: left` property to the `info-container` class so that they are arranged side by side.
   - Ensure each `info-container` fits properly in the available width and wraps to the next line when space is insufficient.

3. **Spacing:**
   - Add 10px of padding inside each `info-container`.
   - Include a margin between each `info-container` to create consistent spacing.

4. **Border and Background:**
   - Add a border and a background color to each `info-container` for visual separation.

5. **Hover Effect:**
   - Include a hover effect to scale up the image when the user hovers over the `info-container`.

## Sample Code

Here’s a sample code snippet to get you started:

### HTML
```html
<div class="gallery">
  <div class="info-container">
    <div class="image-container">
      <img src="path/to/image1.jpg" alt="Image 1">
    </div>
    <div class="text-container">
      <p>Some text information here.</p>
    </div>
  </div>
  <!-- Repeat the above block for 9 more items -->
</div>
```

### CSS
```css
.gallery {
  width: 100%;
}

.info-container {
  float: left;
  width: 30%;
  margin: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  background-color: #f9f9f9;
}

.image-container {
  width: 100%;
}

.text-container {
  width: 100%;
  margin-top: 10px;
}

.info-container img {
  width: 100%;
  height: auto;
}

.info-container:hover img {
  transform: scale(1.1);
  transition: transform 0.3s ease;
}
```
