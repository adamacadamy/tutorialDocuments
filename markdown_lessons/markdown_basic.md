
# Lesson: Markdown Basics (Including Table of Contents)

## Objective:
By the end of this lesson, students will understand the basics of Markdown syntax, including how to create a Table of Contents (TOC), and will be able to write formatted text using Markdown.

### What is Markdown?
Markdown is a lightweight markup language used to add formatting to plain text. Created by John Gruber in 2004, it is popular due to its simplicity and readability.

### Why use Markdown?
- Easy to learn and use.
- Clean, readable text.
- Converts easily to various formats (HTML, PDF, etc.).
- Supported by many platforms (GitHub, Reddit, etc.).

---

## Basic Markdown Syntax

### 1. Headings
You can create headings by adding `#` before your text. The number of `#` symbols indicates the level of the heading.

```markdown
# Heading 1
## Heading 2
### Heading 3
```

This will render as:

# Heading 1  
## Heading 2  
### Heading 3

### 2. Emphasis
You can emphasize text in two ways: italic and bold.

- **Italic**: Use one `*` or `_` around your text.
- **Bold**: Use two `**` or `__` around your text.

```markdown
*Italic Text*
_Italic Text_

**Bold Text**
__Bold Text__
```

This will render as:

*Italic Text*  
**Bold Text**

### 3. Lists

- **Unordered List**: Use `-`, `+`, or `*` followed by a space to create an unordered list.
- **Ordered List**: Use numbers followed by a period.

```markdown
- Item 1
- Item 2
  - Sub-item 1
  - Sub-item 2

1. First item
2. Second item
3. Third item
```

This will render as:

- Item 1
- Item 2
  - Sub-item 1
  - Sub-item 2

1. First item  
2. Second item  
3. Third item

### 4. Links
To create a link, wrap the link text in square brackets `[]`, followed by the URL in parentheses `()`.

```markdown
[OpenAI](https://www.openai.com)
```

This will render as: [OpenAI](https://www.openai.com)

### 5. Images
To add an image, use the same syntax as links but with an exclamation mark `!` before the brackets.

```markdown
![Alt Text](image_url)
```

This will render the image, assuming the URL points to an image file.

### 6. Blockquotes
Use `>` to create a blockquote.

```markdown
> This is a blockquote.
```

This will render as:

> This is a blockquote.

### 7. Code
You can add inline code by wrapping text with backticks `` ` `` or create code blocks by using three backticks ``` before and after the code block.

```markdown
Inline `code`.

```
Code block
```
```

This will render as:

Inline `code`.  
```
Code block
```

### 8. Horizontal Rule
Use three dashes `---`, three asterisks `***`, or three underscores `___` to create a horizontal rule.

```markdown
---
```

This will render as:

---

### 9. Tables
You can create tables by using pipes `|` and dashes `-`. The pipes separate columns, and the dashes create the header.

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Row 1    | Data     |
| Row 2    | Data     |
```

This will render as:

| Header 1 | Header 2 |
|----------|----------|
| Row 1    | Data     |
| Row 2    | Data     |

---

## Creating a Table of Contents

A Table of Contents (TOC) helps readers navigate through your document. In Markdown, you can manually create a TOC by linking to the headings of your document. Here’s how:

### 1. Define Headings
Headings are your main sections, which the TOC will link to.

```markdown
# Introduction
## Features
## Installation
# Conclusion
```

### 2. Add Links to the TOC
To link to a heading, use the heading text in lowercase, replacing spaces with hyphens, and wrap it in square brackets `[]` followed by the link in parentheses `#heading-text`. Example:

```markdown
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Conclusion](#conclusion)
```

This will render as a clickable TOC like this:

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Conclusion](#conclusion)

### Example Document with TOC
```markdown
# My Project

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Conclusion](#conclusion)

## Introduction
This is the introduction section.

## Features
Here are the features.

## Installation
Instructions on how to install.

## Conclusion
Final thoughts and conclusion.
```

This TOC will allow users to click and jump to the corresponding sections.

### Note:
Some platforms, like GitHub, automatically generate a TOC for Markdown files. However, in most Markdown editors and static site generators, you may need to create this manually as described above.

---

## Practical Exercise
1. Create a Markdown file with the following sections:
   - An introduction to a topic of your choice.
   - A list of features or key points.
   - Instructions or guidelines.
   - A conclusion.
2. Add a Table of Contents at the top of the file, linking to each section.
3. Include headings, lists, links, and at least one code block.

---

## Conclusion
Markdown's flexibility allows you to create organized, readable documents easily. Creating a Table of Contents enhances navigation, especially for longer documents. Encourage students to practice creating structured documents with TOCs for better document readability and flow.
