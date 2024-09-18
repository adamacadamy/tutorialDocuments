
# HTML Table Styling Solution

## Solution Description
This solution involves creating tables with various styles, including basic table structure, alternating row colors, and hover effects using CSS.

### Exercise 1: Basic Table Styling

#### 1. **HTML File (`index.html`)**

Create an `index.html` file with the following content to display a table with "Product", "Price", and "Quantity":

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Table Styling</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>Product</th>
                <th>Price</th>
                <th>Quantity</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Apple</td>
                <td>$1</td>
                <td>10</td>
            </tr>
            <tr>
                <td>Banana</td>
                <td>$0.50</td>
                <td>20</td>
            </tr>
            <tr>
                <td>Orange</td>
                <td>$0.80</td>
                <td>15</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
```

#### 2. **CSS File (`styles.css`)**

Create a `styles.css` file to style the table:

```css
/* Basic table styling */
table {
    width: 80%;
    margin: 20px auto;
    border-collapse: collapse;
}

/* Styling for table cells */
th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: center;
}

/* Header styling */
th {
    background-color: #f2f2f2;
}
```

### Exercise 2: Alternating Row Colors

#### 1. **HTML File (`index.html`)**

Extend the previous HTML to create a table with "Name", "Age", and "City" headers:

```html
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>City</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John</td>
            <td>25</td>
            <td>New York</td>
        </tr>
        <tr>
            <td>Jane</td>
            <td>30</td>
            <td>Los Angeles</td>
        </tr>
        <tr>
            <td>Mike</td>
            <td>22</td>
            <td>Chicago</td>
        </tr>
        <tr>
            <td>Emily</td>
            <td>28</td>
            <td>Houston</td>
        </tr>
    </tbody>
</table>
```

#### 2. **CSS File (`styles.css`)**

Add the following styles to handle alternating row colors:

```css
/* Alternating row colors */
tbody tr:nth-of-type(even) {
    background-color: #f9f9f9;
}

/* Header styling */
th {
    background-color: #007bff;
    color: white;
}
```

### Exercise 3: Hover Effects

#### 1. **HTML File (`index.html`)**

Create a table with "Employee ID", "Name", and "Department" headers:

```html
<table>
    <thead>
        <tr>
            <th>Employee ID</th>
            <th>Name</th>
            <th>Department</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>001</td>
            <td>Alice</td>
            <td>HR</td>
        </tr>
        <tr>
            <td>002</td>
            <td>Bob</td>
            <td>Engineering</td>
        </tr>
        <tr>
            <td>003</td>
            <td>Charlie</td>
            <td>Marketing</td>
        </tr>
        <tr>
            <td>004</td>
            <td>David</td>
            <td>Finance</td>
        </tr>
        <tr>
            <td>005</td>
            <td>Eve</td>
            <td>Operations</td>
        </tr>
    </tbody>
</table>
```

#### 2. **CSS File (`styles.css`)**

Add hover effects for table rows:

```css
/* Hover effect for table rows */
tbody tr:hover {
    background-color: #e0f7fa;
    transition: background-color 0.3s ease;
}
```

### Complete CSS Code for All Exercises

Here is the full CSS code combining all the styles:

```css
/* Basic table styling */
table {
    width: 80%;
    margin: 20px auto;
    border-collapse: collapse;
}

/* Styling for table cells */
th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: center;
}

/* Header styling */
th {
    background-color: #007bff;
    color: white;
}

/* Alternating row colors */
tbody tr:nth-of-type(even) {
    background-color: #f9f9f9;
}

/* Hover effect for table rows */
tbody tr:hover {
    background-color: #e0f7fa;
    transition: background-color 0.3s ease;
}
```

This solution meets the requirements of the exercises, demonstrating how to structure and style tables using HTML and CSS, including alternating row colors, hover effects, and proper table cell styling.
