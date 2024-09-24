
# CSS Variables and `@import` in HTML/CSS

## 1. Introduction to CSS Variables

CSS Variables, also known as custom properties, allow you to store values that can be reused throughout your stylesheet. This can be particularly useful for managing colors, spacing, font sizes, and other repetitive values in a more maintainable way.

### 1.1. Defining a CSS Variable

CSS variables are defined within a selector using the `--` prefix. Typically, they are defined in the `:root` selector, which applies globally across your document.

```css
:root {
  --main-bg-color: #3498db;
  --main-text-color: #ffffff;
  --padding-size: 10px;
}
```

- `--main-bg-color`: This defines a color value (`#3498db`), which you can reuse anywhere.
- `--main-text-color`: Another color for the text (`#ffffff`).
- `--padding-size`: A size for padding.

### 1.2. Using CSS Variables

To use a variable, use the `var()` function:

```css
body {
  background-color: var(--main-bg-color);
  color: var(--main-text-color);
  padding: var(--padding-size);
}
```

Here, `var(--main-bg-color)` accesses the value of `--main-bg-color`.

### 1.3. Benefits of CSS Variables

- **Centralized Management:** Variables can be changed in one place, and the changes will reflect throughout your site.
- **Theming:** You can easily create different themes by adjusting just a few variables.
- **Dynamic Changes:** CSS variables can be updated at runtime via JavaScript for responsive or interactive designs.

## 2. Importing CSS Files

The `@import` rule in CSS allows you to include an external CSS file into your current stylesheet. This can help you modularize your CSS code by separating different styles into different files.

### 2.1. Basic Syntax of @import

Here’s the basic syntax for importing a CSS file:

```css
@import url("styles.css");
```

You can also import from a URL:

```css
@import url("https://example.com/styles.css");
```

### 2.2. Importing with Media Queries

You can also specify media queries to apply the imported styles only under certain conditions (e.g., for mobile devices):

```css
@import url("mobile.css") screen and (max-width: 600px);
```

This will apply the `mobile.css` styles only if the screen width is 600px or less.

### 2.3. Performance Considerations

While `@import` can be useful, it can also affect performance since it can delay the loading of CSS files. A better practice for performance is to link stylesheets directly in your HTML `<head>`:

```html
<link rel="stylesheet" href="styles.css">
```

## 3. Combining CSS Variables and Import

You can use `@import` to include a stylesheet where CSS variables are defined, making them available across multiple stylesheets.

### Example

**main.css:**

```css
@import url("variables.css");

body {
  background-color: var(--main-bg-color);
  color: var(--main-text-color);
}
```

**variables.css:**

```css
:root {
  --main-bg-color: #f39c12;
  --main-text-color: #2c3e50;
}
```

In this example, `variables.css` defines the CSS variables, and `main.css` imports that file and applies the variables to style the body.

## 4. Practical Example

Here’s how it all comes together:

### HTML File (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CSS Variables and Import Example</title>
  <link rel="stylesheet" href="main.css">
</head>
<body>
  <h1>Hello World</h1>
  <p>This is a paragraph styled with CSS variables and imports.</p>
</body>
</html>
```

### CSS File (variables.css)

```css
:root {
  --main-bg-color: #2ecc71;
  --main-text-color: #ffffff;
  --heading-font-size: 2rem;
}
```

### CSS File (main.css)

```css
@import url("variables.css");

body {
  background-color: var(--main-bg-color);
  color: var(--main-text-color);
}

h1 {
  font-size: var(--heading-font-size);
  margin-bottom: 10px;
}
```

In this setup:
- The `variables.css` file contains CSS variables.
- The `main.css` imports `variables.css` and applies those variables.

## 5. Conclusion

- CSS Variables help in managing styles more effectively, especially for theming and maintaining consistency.
- The `@import` rule allows modularizing styles, but care should be taken regarding performance.
- Combining both concepts allows for more flexible, reusable, and maintainable code.
