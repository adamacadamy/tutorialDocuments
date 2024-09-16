
# HTML Table Styling Exercises

## Exercise 1: Basic Table Styling
**Objective:** Create a table with headers, rows, and basic styling using CSS.
## 1. Create an HTML table with the following structure:
   - Headers: "Product", "Price", "Quantity"
   - Add at least 3 rows of sample product data.
## 2. Use CSS to:
   - Set the table width to 80%.
   - Apply borders to table cells.
   - Add padding to each cell.
   - Center-align the text in headers.

### Sample Code
```html
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

<style>
table {
  width: 80%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: center;
}
</style>
```

## 3: Alternating Row Colors
**Objective:** Implement alternating row colors for a table to improve readability.
1. Create an HTML table with headers for "Name", "Age", and "City".
2. Add at least 4 rows of sample data.
3. Apply the following CSS styles:
   - Set the background color of every even row to a light gray.
   - Set the text color of table headers to white and use a blue background for them.

## 4: Hover Effects
**Objective:** Add interactive styling with hover effects.
1. Create an HTML table with headers for "Employee ID", "Name", "Department".
2. Add at least 5 rows of sample data.
3. Apply the following CSS styles:
   - Use a light blue background color when hovering over any table row.
   - Use a 0.3-second transition for a smooth hover effect.

 

### Sample Code
```html
<div class="table-container">
  <table>
    <thead>
      <tr>
        <th>Country</th>
        <th>Capital</th>
        <th>Population</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>USA</td>
        <td>Washington, D.C.</td>
        <td>331 million</td>
      </tr>
      <tr>
        <td>Canada</td>
        <td>Ottawa</td>
        <td>38 million</td>
      </tr>
      <tr>
        <td>Japan</td>
        <td>Tokyo</td>
        <td>126 million</td>
      </tr>
    </tbody>
  </table>
</div>

<style>
.table-container {
  overflow-x: auto;
}

table {
  width: 100%;
  min-width: 600px;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
}
</style>
```

## Exercise 2: Basic Table Styling


Your challenge is to create a table using HTML and CSS with the following requirements:

## Requirements

1. Create an HTML table that displays real-world data, such as an employee list.
2. The table should include the following columns:
   - Employee ID
   - Name
   - Department
   - Position
   - Salary
3. Style the table using CSS:
   - Add a background color to the table header.
   - Apply alternating background colors for even rows.
   - Include padding for table cells for a neat appearance.
   - Add a hover effect to highlight rows when the user hovers over them.
4. Do **not** use flexbox or flex-related CSS properties.

## HTML Structure

Create an HTML file with a basic structure for the table as outlined above.

## CSS Styling

Use an external CSS file to style the table according to the requirements. Focus on the following CSS properties:
- `background-color`
- `padding`
- `border-collapse`
- `:nth-of-type` for alternating row colors
- `:hover` for row highlighting

### Tips
- Remember to use semantic HTML tags for the table structure.
- Use the `:nth-of-type` pseudo-class to select and style even rows.
- Keep the styling clean and simple for a professional look.

Save your solution in an HTML file and a CSS file to complete the challenge.