
# CSS Challenge: Change Container Background Based on Media Query

## Challenge Description:
You will define two CSS variables:
- `--background-dark-blue`: for the default dark blue background.
- `--background-light-blue`: for the light blue background when the screen width is less than 600px.

The background color of the `.container` should change based on the screen size:
- Default: Dark blue.
- On smaller screens (less than 600px): Light blue.

### Starter HTML:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CSS Variables Media Query Challenge</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="container">
    <h1>CSS Variables with Media Query</h1>
    <p>Resize the screen to see the container's background color change!</p>
  </div>
</body>
</html>
```

### Starter CSS (styles.css):

```css
:root {
  --background-dark-blue: #1a1a40; /* Dark blue */
  --background-light-blue: #a3d5ff; /* Light blue */
}

body {
  background-color: white;
  margin: 0;
  font-family: Arial, sans-serif;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  text-align: center;
  padding: 20px;
  background-color: var(--background-dark-blue); /* Default background: dark blue */
  color: white;
  border-radius: 10px;
}

/* Media Query: ??? */
@media screen and (max-width: 600px) {
  .container {
    /* Your task: change the background color to light blue */
  }
}
```

### Instructions:
- Use the defined CSS variables to set the `.container` background color.
- Modify the media query to change the `.container` background color to light blue when the screen width is less than 600px.

Good luck!
