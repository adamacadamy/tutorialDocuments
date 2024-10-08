
## Solution

Here's how you can implement the solution:

### Solution CSS (styles.css):

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

/* Media Query: Change background color to light blue on smaller screens */
@media screen and (max-width: 600px) {
  .container {
    background-color: var(--background-light-blue); /* Light blue for small screens */
  }
}
```

### Explanation:

- **CSS Variables**: We defined two CSS variables `--background-dark-blue` and `--background-light-blue` to represent the two background colors.
- **Default State**: By default, the `.container` has a background color of `--background-dark-blue`.
- **Media Query**: When the screen width is less than 600px, the media query kicks in and changes the background color to `--background-light-blue`.
