# Code Challenge: Create a Registration Form

**Objective:**
Build a fully functional registration form using HTML that collects user information, validates inputs, and organizes the data in a user-friendly way.

## Challenge Description

You are tasked with creating a simple registration form for a website. The form will collect the following information from the user:

1. **First Name:** A text input field for the user's first name. This field is required.
2. **Last Name:** A text input field for the user's last name. This field is required.
3. **Email Address:** An email input field where the user can enter their email address. This field is required.
4. **Password:** A password input field to capture a secure password. This field is required.
5. **Age:** A number input field for the user's age, restricted to a range between 18 and 100. This field is required.
6. **Gender:** Radio buttons to allow the user to select their gender (options: Male, Female). This field is required.
7. **Interests:** Checkboxes for the user to select their interests (e.g., Coding, Music, Sports). The user can select multiple options.
8. **Country:** A dropdown list that allows the user to select their country from a predefined list (e.g., United States, Canada, United Kingdom, Australia). This field is required.
9. **Short Bio:** A multi-line text area where the user can write a brief description of themselves.
10. **Experience Level:** A range input that allows the user to rate their experience on a scale of 1 to 10.
11. **Preferred Browser:** An input with a datalist that allows the user to choose their preferred web browser from a list of common browsers (e.g., Chrome, Firefox, Safari, Edge).

## Requirements
- The form should use appropriate HTML5 form elements to capture the data.
- All required fields must include validation.
- The form should include a **Submit** button to send the data and a **Reset** button to clear the form fields.
- The form should be user-friendly and visually organized using appropriate HTML structure (e.g., use of `<fieldset>`, `<legend>`, `<label>` elements).

### Bonus Points
- Implement additional validation using HTML5 attributes (e.g., `pattern`, `maxlength`).
- Style the form using basic CSS to improve the visual appearance.
- Add placeholder text to fields where applicable.

## Submission Guidelines
- Submit the complete HTML code for the registration form.
- Ensure the form is properly indented and commented for clarity.
- Test the form in multiple browsers to ensure compatibility.

## Example Submission

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Form</title>
</head>
<body>
    <h2>Registration Form</h2>
    <form action="/submit_registration" method="POST">
        <!-- Include all the necessary form elements here as described in the challenge -->
    </form>
</body>
</html>
