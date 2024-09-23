
# Web Project Scaffolding and CSS Box Model Challenge

## Challenge Description
In this challenge, you will scaffold a simple web project that includes HTML, CSS, and JavaScript. You'll create the necessary folder structure and files, then style a webpage using text properties and the CSS box model. After that, you will initiate a Git repository and push the project to a new GitHub repository.

### Requirements:
1. **Scaffold the project** by creating the following folder structure:
   ```
   myWebProject/
   ├── css/
   │   └── index.css
   ├── images/
   ├── js/
   │   └── script.js
   ├── index.html
   └── README.md
   ```

2. **Create the `index.html` page**:
   - The `index.html` file should include:
     - A `div` containing a heading, a paragraph, and a button.
     - Proper HTML structure with `head` and `body` tags.
     - A link to your external CSS file located in the `css/` folder. 

3. **Style the page using CSS**:
   - Use the CSS box model to create a card-like design for the `div`.
   - Add styling for:
     - Padding, border, and margin of the `div`.
     - Font size, color, and text alignment of the heading and paragraph.
     - A button that changes its background color when hovered over.

4. **Add Image and style it** Add an image to the `images/` folder and display it inside the `div`. Style the image with a border radius and some padding.
   
5. **Create a `README.md` file** to describe your project:
   - Provide an overview of the project.
   - Include instructions on how to run the project.
   - List the features you've implemented (box model, button interaction, etc.).

6.  **Initiate a Git repository**:
   - Initialize a local Git repository in your project folder.
   - Create a new GitHub repository.
   - Bind the local repository to the new GitHub repository and push the project.

---

## Instructions:

### 1. **Scaffold the Project**:
   - Create the `css/`, `js/`, and `images/` folders.
   - Create the `index.html` file in the root directory.
   - Create `style.css` inside the `css/` folder, and `script.js` inside the `js/` folder.
   - Add a `README.md` file in the root directory.

### 2. **HTML Task (index.html)**:
   - Add a `div` container with a heading, paragraph, and button inside `index.html`.
   - Link your CSS and JavaScript files to the HTML document. 
   - Add an image to the `images/` folder and display it inside the `div`. Style the image with a border radius and some padding.

### 3. **CSS Task (style.css)**:
   - Use the CSS box model to style the `div` (padding, margin, and border).
   - Style the heading and paragraph with different text properties (font size, color, and alignment).
   - Add hover effects to the button.
 

### 4. **Git Task**:
   - **Step 1**: Initialize a Git repository in your project directory by running the following command in your terminal:
     ```bash
     git init
     ```
   - **Step 2**: Add the files to the repository and commit the changes:
     ```bash
     git add .
     git commit -m "Initial commit"
     ```
   - **Step 3**: Create a new repository on GitHub and copy the repository URL (either HTTPS or SSH).
   - **Step 4**: Bind your local repository to the remote GitHub repository:
     ```bash
     git remote add origin <repository-URL>
     ```
   - **Step 5**: Push your local repository to GitHub:
     ```bash
     git push -u origin master
     ```



---

## Example HTML Structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Web Project</title>
  <link rel="stylesheet" href="css/index.css">
</head>
<body>
  <div class="card">
    <h1>Welcome to the Challenge</h1>
     <img src="funny_camel.png" alt="funny camel">

    <p>This is a simple box model design with styled text properties.</p>
    <button>Click Me</button>
  </div> 
</body>
</html>
```

---

## Example CSS (style.css):

```css
body {
  font-family: Arial, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  background-color: #f0f0f0;
}

.card {
  background-color: white;
  padding: 20px;
  border: 2px solid #ccc;
  margin: 20px;
  width: 300px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 24px;
  color: #333;
  margin-bottom: 10px;
}

p {
  font-size: 16px;
  color: #666;
  margin-bottom: 20px;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  border: none;
  color: white;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}
```

---

 