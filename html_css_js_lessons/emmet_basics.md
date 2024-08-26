# Emmet Shortcuts for HTML

Emmet is a plugin for text editors that provides shortcuts for writing HTML, CSS, and other languages. It allows you to expand simple abbreviations into complex code structures. Below is a tutorial that covers the basics of Emmet shortcuts for HTML, along with some examples.

## Basic Emmet Abbreviations for HTML

1. **Basic HTML Boilerplate:**
   - Type `!` and then press `Tab` or `Enter` (depending on your editor).
   - This expands to a full HTML boilerplate code:
     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Document</title>
     </head>
     <body>
         
     </body>
     </html>
     ```

2. **Creating Tags:**
   - Simply type the tag name and press `Tab` or `Enter`.
   - Example: `div` expands to:
     ```html
     <div></div>
     ```

3. **Nesting Elements:**
   - Use the `>` symbol to nest elements inside one another.
   - Example: `div>ul>li` expands to:
     ```html
     <div>
         <ul>
             <li></li>
         </ul>
     </div>
     ```

4. **Siblings:**
   - Use the `+` symbol to create sibling elements.
   - Example: `div+p+bq` expands to:
     ```html
     <div></div>
     <p></p>
     <blockquote></blockquote>
     ```

5. **Adding Attributes:**
   - Use `[]` brackets to add attributes to tags.
   - Example: `a[href="https://example.com"]` expands to:
     ```html
     <a href="https://example.com"></a>
     ```

6. **Classes and IDs:**
   - Use `.` for classes and `#` for IDs.
   - Example: `div.classname` expands to:
     ```html
     <div class="classname"></div>
     ```
   - Example: `div#idname` expands to:
     ```html
     <div id="idname"></div>
     ```

7. **Multiplying Elements:**
   - Use the `*` symbol followed by a number to create multiple elements.
   - Example: `ul>li*3` expands to:
     ```html
     <ul>
         <li></li>
         <li></li>
         <li></li>
     </ul>
     ```

8. **Grouping:**
   - Use `()` to group elements together.
   - Example: `(div>ul>li)*2` expands to:
     ```html
     <div>
         <ul>
             <li></li>
         </ul>
     </div>
     <div>
         <ul>
             <li></li>
         </ul>
     </div>
     ```

## Advanced Emmet Shortcuts

1. **Numbering Items:**
   - Use `$` to insert numbering.
   - Example: `ul>li.item$*3` expands to:
     ```html
     <ul>
         <li class="item1"></li>
         <li class="item2"></li>
         <li class="item3"></li>
     </ul>
     ```

2. **Custom Numbering:**
   - Use `[1-9]` inside curly braces to specify custom numbering.
   - Example: `ul>li.item${a}*3` expands to:
     ```html
     <ul>
         <li class="itema"></li>
         <li class="itemb"></li>
         <li class="itemc"></li>
     </ul>
     ```

3. **Lorem Ipsum:**
   - Use `lorem` to generate lorem ipsum text.
   - Example: `p>lorem` expands to:
     ```html
     <p>Lorem ipsum dolor sit amet...</p>
     ```
   - You can specify the number of words, e.g., `lorem10` will generate 10 words.

4. **Implicit Tag Names:**
   - Emmet allows you to omit tag names for some elements (like `div`).
   - Example: `.container` expands to:
     ```html
     <div class="container"></div>
     ```

## Popular Editors Supporting Emmet

- **Visual Studio Code:** Emmet is built-in, and you can trigger Emmet abbreviations by typing an abbreviation and pressing `Tab`.
- **Sublime Text:** Emmet can be installed via Package Control.
- **Atom:** Emmet is also available as a plugin.
- **Brackets:** Supports Emmet with a plugin.

## Tips

- **Autocompletion:** Emmet often works alongside your editor’s autocompletion. You can disable or tweak these settings if Emmet conflicts with other features.
- **Customizing Emmet:** You can customize Emmet’s behavior in your editor by modifying the settings, such as defining new snippets or changing the trigger key.

## Practice Examples

Try expanding the following abbreviations in your editor:

1. `header>nav>ul>li*3>a[href="#"]`
2. `.container>header+main+footer`
3. `section#main>h1.title+p+ul>li*4`

This will help solidify your understanding of Emmet shortcuts for HTML.

For more details, you can always visit the official [Emmet documentation](https://emmet.io/).
