
# HTML Basics
![alt text](images/html.png)
## What is HTML?

**HTML (Hypertext Markup Language)** is the standard language used to create webpages. It allows you to structure content on the web by using a series of elements. These elements are represented by tags, usually with an opening and closing tag, and the content is placed between these tags.

### Breaking Down HTML:

- **Hypertext**: This refers to text that contains links to other texts or resources. In HTML, you use hyperlinks (`<a>` tags) to connect different pages, allowing users to navigate through various parts of a website or even across the web.
  
- **Text**: The content inside the tags is often text. This text is what will be displayed on the page, formatted according to the HTML tags surrounding it.
  
- **Markup**: HTML is a markup language, which means it uses tags to "mark up" the text. These tags tell the web browser how to display the content, such as making text bold, creating a list, or embedding an image. The tags are part of the markup but are not shown to the user; they only control how the content looks.

In summary, **HTML** allows you to combine links (hypertext) with content (text), structured by tags (markup), to create webpages.

## Structure of an HTML Document

A basic HTML document follows this structure:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
```

### Explanation:
1. **`<!DOCTYPE html>`**: Declares the document as an HTML5 document.
2. **`<html>`**: The root element that wraps all content on the page.
3. **`<head>`**: Contains meta-information about the document, such as the title.
4. **`<title>`**: Defines the title of the webpage, shown in the browser tab.
5. **`<body>`**: Contains the visible content of the webpage.

## Common HTML Elements

### Headings

HTML provides six levels of headings, from `<h1>` (most important) to `<h6>` (least important):

```html
<h1>This is an H1 Heading</h1>
<h2>This is an H2 Heading</h2>
<h3>This is an H3 Heading</h3>
<h4>This is an H4 Heading</h4>
<h5>This is an H5 Heading</h5>
<h6>This is an H6 Heading</h6>
```

### Paragraphs

Paragraphs are defined using the `<p>` tag:

```html
<p>This is a paragraph of text.</p>
```

### Links

Links are created using the `<a>` tag. The `href` attribute specifies the URL of the page the link goes to:

```html
<a href="https://www.example.com">This is a link</a>
```

### Images

Images are added using the `<img>` tag. The `src` attribute defines the path to the image, and the `alt` attribute provides alternative text:

```html
<img src="image.jpg" alt="Description of the image">
```

### Lists

There are two types of lists in HTML: **ordered lists** and **unordered lists**.

#### Unordered List:
```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```

#### Ordered List:
```html
<ol>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ol>
```

### Tables

HTML tables are created using the `<table>` tag. You use `<tr>` for table rows, `<th>` for table headers, and `<td>` for table cells:

```html
<table>
  <tr>
    <th>Header 1</th>
    <th>Header 2</th>
  </tr>
  <tr>
    <td>Data 1</td>
    <td>Data 2</td>
  </tr>
</table>
```

### Forms

Forms collect user input and can be submitted to a server. Here’s a basic form structure:

```html
<form action="/submit" method="post">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name">

  <label for="email">Email:</label>
  <input type="email" id="email" name="email">

  <input type="submit" value="Submit">
</form>
```

### Div and Span

- **`<div>`**: A block-level container used to group elements for styling or layout purposes.
- **`<span>`**: An inline container for styling a small piece of text or content within a block-level element.

```html
<div>
  <p>This is inside a div element.</p>
</div>

<p>This is a <span>span element</span> inside a paragraph.</p>
```

## Attributes

HTML tags can have attributes that provide additional information about elements. Common attributes include:

- **`href`**: Specifies the URL for a link.
- **`src`**: Specifies the source of an image or media file.
- **`alt`**: Provides alternative text for images.
- **`id`**: Assigns a unique identifier to an element.
- **`class`**: Specifies a class name for CSS styling.

Example:

```html
<a href="https://example.com" class="button-link">Click Here</a>
<img src="image.png" alt="Example Image">
```

## Semantic HTML

Semantic HTML introduces elements that clearly describe their meaning, improving accessibility and SEO.

Some common semantic tags:

- **`<header>`**: Represents the header section of a webpage or a section.
- **`<nav>`**: Defines a navigation menu.
- **`<main>`**: The main content of the document.
- **`<section>`**: Defines a section within a document.
- **`<article>`**: Represents an independent piece of content.
- **`<footer>`**: Represents the footer of a page or section.

Example:

```html
<header>
  <h1>Website Title</h1>
  <nav>
    <a href="#home">Home</a>
    <a href="#about">About</a>
  </nav>
</header>
<main>
  <section>
    <h2>Introduction</h2>
    <p>This is an introductory section.</p>
  </section>
  <article>
    <h2>Article Title</h2>
    <p>This is an article.</p>
  </article>
</main>
<footer>
  <p>&copy; 2024 Your Website</p>
</footer>
```

## Comments

You can add comments to your HTML code using `<!-- -->`:

```html
<!-- This is a comment -->
```

Comments are ignored by the browser and can be useful for documentation.

## Conclusion

This is just the beginning of your journey with HTML. As you explore more, you'll learn about advanced concepts like CSS for styling, JavaScript for interactivity, and how to build fully responsive, dynamic websites. Happy coding!
