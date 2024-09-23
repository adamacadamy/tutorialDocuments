
# CSS Flexbox Model Tutorial

## 1. What is Flexbox?
Flexbox is short for "Flexible Box Layout," and it is used to design layouts in a more flexible and efficient way, especially for laying out elements within a container.

## 2. Basic Concepts of Flexbox
Flexbox operates on a container and its children. The container is called the **flex container**, and its children are **flex items**.

To start using Flexbox, you need to define a flex container:

```html
<div class="container">
  <div class="item">Item 1</div>
  <div class="item">Item 2</div>
  <div class="item">Item 3</div>
</div>
```

To turn the container into a flex container, you apply the `display: flex;` property:

```css
.container {
  display: flex;
}
```

## 3. Main Axis and Cross Axis
- **Main Axis**: This is the primary axis along which flex items are placed. By default, it runs horizontally from left to right.
- **Cross Axis**: Perpendicular to the main axis, this is the vertical axis by default.

You can change the main axis by using the `flex-direction` property.

## 4. Properties for the Flex Container

### 4.1. `flex-direction`
Defines the direction in which the flex items are placed in the container.

```css
.container {
  display: flex;
  flex-direction: row; /* Default, horizontal layout */
}
```

Other values:
- `row-reverse`: Right to left
- `column`: Top to bottom
- `column-reverse`: Bottom to top

### 4.2. `justify-content`
Aligns the flex items along the main axis.

```css
.container {
  display: flex;
  justify-content: space-between;
}
```

Values:
- `flex-start`: Align items to the start of the container (default)
- `flex-end`: Align items to the end
- `center`: Center items
- `space-between`: Space between items evenly
- `space-around`: Space around items

### 4.3. `align-items`
Aligns flex items along the cross axis.

```css
.container {
  display: flex;
  align-items: center;
}
```

Values:
- `stretch`: Stretch items to fill the container (default)
- `flex-start`: Align items to the start of the cross axis
- `flex-end`: Align items to the end of the cross axis
- `center`: Center items on the cross axis

### 4.4. `flex-wrap`
By default, flex items are all placed in one line. `flex-wrap` allows them to wrap onto multiple lines.

```css
.container {
  display: flex;
  flex-wrap: wrap;
}
```

Values:
- `nowrap`: All items in one line (default)
- `wrap`: Items wrap onto multiple lines
- `wrap-reverse`: Items wrap onto multiple lines in reverse order

## 5. Properties for the Flex Items

### 5.1. `flex-grow`
Defines how much a flex item should grow relative to the other items.

```css
.item {
  flex-grow: 1;
}
```

### 5.2. `flex-shrink`
Defines how much a flex item should shrink relative to the other items.

```css
.item {
  flex-shrink: 1;
}
```

### 5.3. `flex-basis`
Defines the initial size of a flex item before any growing or shrinking.

```css
.item {
  flex-basis: 100px;
}
```

## 6. Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flexbox Example</title>
  <style>
    .container {
      display: flex;
      flex-direction: row;
      justify-content: space-around;
      align-items: center;
      flex-wrap: wrap;
      height: 300px;
      background-color: lightgray;
    }
    .item {
      background-color: lightblue;
      padding: 20px;
      flex-grow: 1;
      margin: 10px;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="item">Item 1</div>
    <div class="item">Item 2</div>
    <div class="item">Item 3</div>
  </div>
</body>
</html>
```

## 7. Summary
- **Flex container**: Use `display: flex;` to create a flex container.
- **Direction**: Control the direction of items using `flex-direction`.
- **Alignment**: Use `justify-content` for horizontal alignment and `align-items` for vertical alignment.
- **Flex properties**: Control the size and spacing of items with properties like `flex-grow`, `flex-shrink`, and `flex-basis`.

This should give you a solid foundation to start using Flexbox!
