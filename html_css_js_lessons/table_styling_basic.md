
# HTML CSS Lesson: Styling Tables

## Basic HTML Table Structure
Here's a basic HTML table to start with:
```html
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Age</th>
      <th>Occupation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>John Doe</td>
      <td>28</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <td>Jane Smith</td>
      <td>34</td>
      <td>Designer</td>
    </tr>
    <tr>
      <td>Mike Johnson</td>
      <td>45</td>
      <td>Manager</td>
    </tr>
  </tbody>
</table>
```

## Basic Table Styling
To apply some basic styles to the table, we can add the following CSS:
```css
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

th {
  background-color: #f2f2f2;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}
```

### Explanation of Basic Styles
- **`table`**: Sets the width of the table to 100% and collapses the borders for a cleaner look.
- **`th, td`**: Adds a border to table cells and applies padding for better readability.
- **`th`**: Sets the background color of the header row.
- **`tr:nth-child(even)`**: Alternates the background color of table rows for easy distinction.

## Advanced Table Styling
Now, let's add more styling elements like hover effects, rounded corners, and more:
```css
table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  font-size: 18px;
  text-align: left;
}

th, td {
  border: 1px solid #dddddd;
  padding: 12px 15px;
}

th {
  background-color: #009879;
  color: #ffffff;
}

tr {
  transition: background-color 0.2s ease;
}

tr:hover {
  background-color: #f1f1f1;
}

tr:nth-child(even) {
  background-color: #f3f3f3;
}

table, th, td {
  border-radius: 5px;
}
```

### Explanation of Advanced Styles
- **`transition`**: Adds a smooth transition effect when hovering over table rows.
- **`hover` effect**: Changes the background color of rows when the user hovers over them.
- **Rounded corners**: Uses `border-radius` to give table, header, and cells rounded edges for a modern look.
