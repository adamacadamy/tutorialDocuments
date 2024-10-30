import re
import math

# Regular Expressions: Advanced Exercises

# 11. Write a function that extracts all HTML tags from a given text.
# Example text: "<div>Hello</div><p>World</p>"
def extract_html_tags(text):
    # Your code here
    pass

# 12. Create a regex to validate a complex password with the following requirements:
# - At least 8 characters
# - Contains both uppercase and lowercase letters
# - Contains at least one digit
# - Contains at least one special character (!@#$%^&*)
def is_complex_password(password):
    # Your code here
    pass

# 13. Write a regex to find all email addresses with a specific domain, e.g., "@example.com".
# Example text: "Contact us at admin@example.com or support@example.com."
domain_text = "Contact us at admin@example.com or support@example.com."
# Your code here

# 14. Create a regex pattern to extract all hyperlinks from an HTML page.
# Example text: '<a href="http://example.com">Example</a><a href="https://google.com">Google</a>'
html_text = '<a href="http://example.com">Example</a><a href="https://google.com">Google</a>'
# Your code here

# 15. Write a regex pattern to validate a US Social Security Number (SSN) in the format "XXX-XX-XXXX".
# Example: "123-45-6789"
def is_valid_ssn(ssn):
    # Your code here
    pass

# 16. Create a regex pattern that matches a string only if it contains both 'foo' and 'bar' in any order.
# Example text: "foobar", "barfoo", "foo something bar"
def contains_foo_and_bar(text):
    # Your code here
    pass

# 17. Write a regex pattern to find and replace all instances of currency symbols ($, €, £) in a text with 'USD'.
# Example text: "The price is $10, £5, and €7."
currency_text = "The price is $10, £5, and €7."
# Your code here

# 18. Write a function that removes all punctuation marks from a given text.
# Example text: "Hello, world! How's it going?"
def remove_punctuation(text):
    # Your code here
    pass

# 19. Create a regex pattern that extracts the filename from a file path.
# Example path: "/home/user/docs/report.pdf" should return "report.pdf".
file_path = "/home/user/docs/report.pdf"
# Your code here

# 20. Write a regex that captures and returns any repeated words in a sentence.
# Example sentence: "This is is a test test sentence."
repeated_text = "This is is a test test sentence."
# Your code here


# Object-Oriented Programming: Advanced Exercises

# 21. Define a 'Transaction' class to represent a bank transaction with attributes for amount, date, and type (deposit/withdrawal).
# Implement methods to validate the transaction and display the transaction details.
class Transaction:
    # Your code here
    pass

# 22. Create a 'School' class with methods to add students, remove students, and calculate the average grade of all students.
# Each student should be an instance of the 'Student' class from Exercise 2.
class School:
    # Your code here
    pass

# 23. Write a class 'Inventory' that manages a collection of products.
# Implement methods to add products, remove products, and find a product by name.
class Inventory:
    # Your code here
    pass

# 24. Define a 'Matrix' class that allows you to add, subtract, and multiply matrices.
# Implement the necessary methods to handle these operations with error checking.
class Matrix:
    # Your code here
    pass

# 25. Create a 'Calculator' class with static methods for addition, subtraction, multiplication, and division.
# Then, create a subclass 'ScientificCalculator' that adds methods for square root and power calculations.
class Calculator:
    # Your code here
    pass

class ScientificCalculator(Calculator):
    # Your code here
    pass

# 26. Define a 'Library' class that supports lending books.
# Track which books are available and which are lent out to specific users.
class Library:
    # Your code here
    pass

# 27. Write a 'ChatRoom' class that allows users to join, leave, and send messages to each other.
# Each user should be an instance of a 'User' class that stores their name and any messages sent.
class ChatRoom:
    # Your code here
    pass

class User:
    # Your code here
    pass

# 28. Create an 'Order' class that represents an e-commerce order with items, quantities, and prices.
# Implement a method to calculate the total order amount, including tax and shipping.
class Order:
    # Your code here
    pass

# 29. Define a 'FileProcessor' class that reads, writes, and appends data to a file.
# Implement methods for each operation with proper error handling.
class FileProcessor:
    # Your code here
    pass

# 30. Write a 'Tournament' class that manages teams and scores.
# Implement methods to add teams, record match results, and display the leaderboard.
class Tournament:
    # Your code here
    pass
