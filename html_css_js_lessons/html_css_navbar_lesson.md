
# How to Style a Navigation Bar with `<ul>` and `<li>` for Internal and External (Section) Links

## **Part 1: Setting Up the Basic HTML Structure**

First, we'll create a simple HTML file that includes an unordered list (`<ul>`) to define the navigation bar. The list items (`<li>`) will contain both internal links (navigation between different pages) and "external" submenu links that navigate to sections within the same page.

**HTML (`index.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styled Navigation Bar</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation Bar -->
    <nav>
        <ul class="navbar">
            <li><a href="index.html">Home</a></li> <!-- Internal link -->
            <li><a href="about.html">About</a></li> <!-- Internal link -->
            <li><a href="#services">Services</a> <!-- External submenu -->
                <ul class="submenu">
                    <li><a href="#web-design">Web Design</a></li>
                    <li><a href="#seo">SEO</a></li>
                    <li><a href="#marketing">Marketing</a></li>
                </ul>
            </li>
            <li><a href="#contact">Contact</a></li> <!-- Internal section link -->
        </ul>
    </nav>

    <!-- Content Sections -->
    <section id="services">
        <h2>Services</h2>
        <p>Our range of services.</p>
        <div id="web-design">
            <h3>Web Design</h3>
            <p>Information about web design services.</p>
        </div>
        <div id="seo">
            <h3>SEO</h3>
            <p>Information about SEO services.</p>
        </div>
        <div id="marketing">
            <h3>Marketing</h3>
            <p>Information about marketing services.</p>
        </div>
    </section>

    <section id="contact">
        <h2>Contact Us</h2>
        <p>Get in touch with us.</p>
    </section>
</body>
</html>
```

**Explanation:**
- This navigation bar includes internal links to other pages (`index.html`, `about.html`) and internal section links (`#services`, `#contact`).
- The "Services" link has a nested unordered list (`<ul class="submenu">`) to create a submenu for external links to sections within the page (e.g., `#web-design`, `#seo`, `#marketing`).

---

## **Part 2: Styling the Navigation Bar Using CSS**

We'll now use CSS to style the navigation bar and submenu.

**CSS (`styles.css`):**
```css
/* Basic Reset */
body {
    margin: 0;
    font-family: Arial, sans-serif;
}

/* Navigation Bar */
.navbar {
    list-style-type: none; /* Remove bullet points */
    margin: 0;
    padding: 0;
    background-color: #333; /* Dark background color */
    overflow: hidden; /* Clear floats */
    text-align: center; /* Center text */
}

/* Navigation Items */
.navbar > li {
    display: inline-block; /* Place items side by side */
    position: relative; /* To position the submenu */
}

/* Links in the Navbar */
.navbar > li > a {
    display: block; /* Make the entire area clickable */
    color: white;
    text-decoration: none;
    padding: 14px 20px;
}

/* Hover Effect */
.navbar > li > a:hover {
    background-color: #555;
}

/* Submenu */
.submenu {
    list-style-type: none; /* Remove bullet points */
    padding: 0;
    margin: 0;
    position: absolute; /* Position relative to the parent */
    top: 100%; /* Position below the parent */
    left: 0;
    background-color: #333;
    display: none; /* Hide submenu by default */
    text-align: left; /* Align text in submenu */
}

/* Submenu Items */
.submenu li {
    width: 150px; /* Set width for submenu items */
}

/* Links in the Submenu */
.submenu li a {
    display: block;
    color: white;
    padding: 10px;
    text-decoration: none;
}

/* Show Submenu on Hover */
.navbar > li:hover .submenu {
    display: block;
}

/* Hover Effect for Submenu Items */
.submenu li a:hover {
    background-color: #555;
}

/* Section Styles */
section {
    padding: 20px;
    margin: 20px;
}
```

**Explanation:**
- **`.navbar > li`**: Uses `display: inline-block` to place navigation items side by side and `position: relative` to position the submenu.
- **`.submenu`**: The submenu (`<ul>`) is absolutely positioned and hidden by default (`display: none`).
- **`.navbar > li:hover .submenu`**: When a user hovers over a navigation item that has a submenu, the submenu is shown (`display: block`).
- **`.submenu li a`**: Styles the links in the submenu, adding padding and a hover effect.

---

## **Part 3: Adding More Styles and Adjustments**

You can further customize the appearance of the navigation bar and submenu using additional CSS properties.

### **Optional: Fixed Navigation Bar**

To make the navigation bar stick to the top of the page:
```css
.navbar {
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 1000;
}
```

### **Spacing Around Sections**

Add padding or margin to the content sections to avoid overlapping with the fixed navigation bar:
```css
section {
    padding: 60px 20px;
    margin-top: 50px;
}
```

---

## **Conclusion**

In this tutorial, you learned how to:
1. Create a **navigation bar** using an unordered list (`<ul>` and `<li>`).
2. Add internal links for navigation between different pages.
3. Create **submenus** for external section links within the same page.
4. Style the navigation bar and submenu using **CSS** without JavaScript or Flexbox.
5. Add hover effects and make the navigation bar fixed at the top of the page.
