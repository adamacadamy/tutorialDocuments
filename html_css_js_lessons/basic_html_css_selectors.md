
# Basic HTML and CSS Selectors

## 1. **Element Selector**
Targets all elements of a specific type.

```html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```

```css
p {
  color: blue;
}
```

- **Effect**: All `<p>` elements will have blue text.

## 2. **Class Selector**
Targets elements with a specific class.

```html
<div class="box">Box 1</div>
<div class="box">Box 2</div>
```

```css
.box {
  background-color: lightgray;
}
```

- **Effect**: Both divs with the class `box` will have a light gray background.

## 3. **ID Selector**
Targets an element with a specific ID. IDs are unique, meaning they should only be used once per page.

```html
<div id="main-content">This is the main content</div>
```

```css
#main-content {
  font-size: 20px;
}
```

- **Effect**: The element with the ID `main-content` will have a font size of 20px.

## 4. **Universal Selector**
Targets all elements on the page.

```css
* {
  margin: 0;
  padding: 0;
}
```

- **Effect**: Resets all margins and paddings on every element to zero.

## 5. **Attribute Selector**
Targets elements based on their attributes.

```html
<a href="https://example.com" target="_blank">External Link</a>
<a href="/about">Internal Link</a>
```

```css
a[target="_blank"] {
  color: red;
}
```

- **Effect**: The external link with `target="_blank"` will have red text.

## 6. **Descendant Selector**
Targets elements that are nested within another element.

```html
<div class="container">
  <p>Paragraph inside container.</p>
</div>
<p>Paragraph outside container.</p>
```

```css
.container p {
  color: green;
}
```

- **Effect**: Only the paragraph inside the `container` class will be green.

## 7. **Child Selector**
Targets only direct children of a specific element.

```html
<ul>
  <li>Item 1</li>
  <li>Item 2
    <ul>
      <li>Nested Item 1</li>
    </ul>
  </li>
</ul>
```

```css
ul > li {
  color: blue;
}
```

- **Effect**: Only direct `li` elements (like Item 1 and 2) will be blue, not the nested item.

## 8. **Group Selector**
Targets multiple selectors at once.

```html
<h1>Title</h1>
<p>Paragraph</p>
```

```css
h1, p {
  text-align: center;
}
```

- **Effect**: Both the `h1` and `p` elements will have centered text.

## 9. **Pseudo-Class Selector**
Targets elements based on their state, such as `hover`, `focus`, `first-child`, etc.

```html
<a href="#">Hover over me</a>
```

```css
a:hover {
  color: green;
}
```

- **Effect**: The link will turn green when hovered over.

## 10. **Pseudo-Element Selector**
Targets parts of an element, such as the first letter or first line.

```html
<p>First letter of this paragraph will be large.</p>
```

```css
p::first-letter {
  font-size: 2em;
  color: red;
}
```

- **Effect**: The first letter of the paragraph will be larger and red.
