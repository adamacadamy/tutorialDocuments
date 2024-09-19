
# Lesson: Styling Forms with Pure CSS (Without Flexbox)

#### **Objective:**
Learn how to create and style a form using pure CSS without relying on Flexbox. This lesson will teach you how to structure and style form elements such as inputs, labels, buttons, and text areas using traditional CSS properties like margins, paddings, and float.

#### **Prerequisites:**
- Basic understanding of HTML structure
- Basic knowledge of CSS selectors and properties

---

### **Step 1: Creating the Basic Form Structure with HTML**

First, let’s create an HTML form with text fields, a text area, and a submit button.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css"> <!-- Link to the CSS file -->
    <title>Styled Form</title>
</head>
<body>
    <!-- Form Container -->
    <div class="form-container">
        <form action="#" method="post">
            <h2>Contact Us</h2>

            <!-- Name Field -->
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>

            <!-- Email Field -->
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>

            <!-- Message Field -->
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>
            </div>

            <!-- Submit Button -->
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>
```

**Explanation:**
- Each input field and text area is wrapped in a `<div>` with the class `form-group` for easier styling and layout control.
- Labels are directly associated with input fields using the `for` attribute.

---

### **Step 2: Styling the Form with Pure CSS (No Flexbox)**

Here’s the CSS code to style the form using basic CSS properties without using Flexbox.

```css
/* Basic Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Styling the form container */
.form-container {
    width: 100%;
    max-width: 500px;
    margin: 50px auto; /* Centers the form on the page */
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Styling form elements */
form {
    width: 100%;
}

h2 {
    text-align: center;
    margin-bottom: 20px;
    color: #333;
}

/* Form Group Styling */
.form-group {
    margin-bottom: 15px;
}

/* Label Styling */
label {
    display: block; /* Forces label to take up the full width */
    margin-bottom: 5px;
    font-size: 16px;
    color: #333;
}

/* Input and Textarea Styling */
input,
textarea {
    width: 100%; /* Makes input fields take full width of the container */
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
}

/* Focus Effect */
input:focus,
textarea:focus {
    border-color: #007bff;
    outline: none;
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

/* Submit Button Styling */
button {
    display: block;
    width: 100%; /* Makes the button take full width of the form */
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-top: 10px;
}

button:hover {
    background-color: #0056b3;
}
```

**Explanation:**
1. **Basic Reset**: The `*` selector resets the default margin, padding, and sets `box-sizing` to `border-box` for consistent layout control.
2. **Form Container**: 
    - `.form-container` centers the form on the page with `margin: 50px auto;` and applies padding, background color, rounded corners, and a shadow.
3. **Form Group**: 
    - `.form-group` wraps each label-input pair and uses `margin-bottom` to create space between each field.
4. **Labels**:
    - `label` is styled with `display: block` to make it occupy the full width, allowing the input to be placed below it.
5. **Input and Textarea**:
    - `width: 100%` makes the input fields fill the container's width, ensuring a uniform appearance.
6. **Button**:
    - Styled with `display: block` and `width: 100%` to make it occupy the full width of the container.
    - Adds a smooth transition effect on hover using `background-color` and `transition`.

---

### **Step 3: Testing and Customizing**
1. Save the HTML and CSS code in separate files (`.html` and `styles.css`).
2. Open the HTML file in a web browser to see the styled form.
3. You can tweak padding, colors, margins, and borders in the CSS to match your design preferences.

### **Activity**
1. Add new fields like a dropdown (`<select>`), checkboxes, or radio buttons.
2. Modify the CSS to include styles for these new elements, such as controlling their width, padding, and border.

### **Key Takeaways**
- Forms can be styled with pure CSS using basic properties like `display`, `margin`, `padding`, and `width`.
- The `display: block` property is useful for making labels and buttons occupy the full width of their containers.
- CSS properties like `border-radius` and `box-shadow` enhance the form's appearance and make it more user-friendly.

Feel free to experiment with the styling to create different themes and layouts for your forms!
