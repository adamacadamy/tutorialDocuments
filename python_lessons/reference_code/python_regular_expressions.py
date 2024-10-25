 
# Regular Expressions (Regex) - Python Lesson from 0 to Hero

# 1. Introduction to Regular Expressions
# A regular expression is a special sequence of characters that helps you match or find
# other strings or sets of strings using a specialized syntax. It's commonly used in text
# processing tasks, like searching, replacing, or validating data.

# In Python, the re module provides support for regular expressions.
import re

# The main functions provided by the re module are:
# - re.match(): checks for a match only at the beginning of the string.
# - re.search(): searches for a match anywhere in the string.
# - re.findall(): returns a list of all non-overlapping matches in the string.
# - re.sub(): replaces matches with a new string.
# - re.split(): splits a string by the occurrences of a pattern.

# 2. Basic Syntax

# Special Characters:
# - . matches any character except a newline
# - ^ matches the beginning of a string
# - $ matches the end of a string
# - * matches 0 or more repetitions
# - + matches 1 or more repetitions
# - ? matches 0 or 1 repetition
# - {} specifies the number of repetitions
# - [] matches any single character in brackets
# - | OR operator
# - \\ escapes special characters

# Example Patterns
pattern = r"hello"    # Match the exact word 'hello'
pattern = r"\\d"       # Match any digit (0-9)
pattern = r"\\w"       # Match any word character (a-z, A-Z, 0-9, _)
pattern = r"\\s"       # Match any whitespace (spaces, tabs, newlines)

# 3. Using Basic Patterns

# Example: Finding a Simple Match
text = "hello world"
pattern = r"hello"
match = re.search(pattern, text)
if match:
    print("Found:", match.group())  # Outputs: Found: hello

# 4. Anchors

# Anchors are used to match positions within the text.
# ^ matches the start of the string.
# $ matches the end of the string.

# Match if string starts with 'hello'
re.search(r"^hello", "hello world")

# Match if string ends with 'world'
re.search(r"world$", "hello world")

# 5. Quantifiers

# Quantifiers define how many instances of a character or group are allowed.
# - * matches 0 or more occurrences
# - + matches 1 or more occurrences
# - ? matches 0 or 1 occurrence
# - {n} matches exactly n occurrences
# - {n,} matches n or more occurrences
# - {n,m} matches between n and m occurrences

# Match one or more digits
re.search(r"\\d+", "123abc")  # Matches: 123

# Match exactly 3 digits
re.search(r"\\d{3}", "abc123")  # Matches: 123

# 6. Character Classes and Ranges

# Character classes are used to specify a set of characters.
# - [abc] matches a, b, or c.
# - [a-z] matches any lowercase letter from a to z.
# - [^abc] matches any character except a, b, or c.

# Match any vowel
re.search(r"[aeiou]", "hello")  # Matches: e

# Match any lowercase letter
re.findall(r"[a-z]", "Hello World")  # Matches: ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']

# 7. Grouping and Capturing

# Use parentheses () to group parts of a pattern and capture matched substrings.

text = "John Doe, age 30"
pattern = r"(\\w+)\\s(\\w+),\\sage\\s(\\d+)"
match = re.search(pattern, text)

if match:
    print(match.group(1))  # John
    print(match.group(2))  # Doe
    print(match.group(3))  # 30

# 8. Named Groups

# Named groups make patterns more readable.

pattern = r"(?P<first_name>\\w+)\\s(?P<last_name>\\w+)"
match = re.search(pattern, "John Doe")
if match:
    print(match.group("first_name"))  # John
    print(match.group("last_name"))   # Doe

# 9. Lookaheads and Lookbehinds

# These are zero-width assertions that don’t consume characters in the string.
# - Lookahead: (?=...)
# - Negative Lookahead: (?!...)
# - Lookbehind: (?<=...)
# - Negative Lookbehind: (?<!...)

# Match 'John' only if it's followed by ' Doe'
re.search(r"John(?= Doe)", "John Doe")  # Matches: John

# Match 'Doe' only if it's not preceded by 'John '
re.search(r"(?<!John )Doe", "Jane Doe")  # Matches: Doe

# 10. Common Use Cases

# a) Validating Email Addresses
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"

# b) Replacing Text
text = "The rain in Spain"
pattern = r"rain"
new_text = re.sub(pattern, "sun", text)
print(new_text)  # Outputs: The sun in Spain

# c) Splitting Text
text = "apple, banana; grape|orange"
pattern = r"[,;|]"
result = re.split(pattern, text)
print(result)  # Outputs: ['apple', 'banana', 'grape', 'orange']

# 11. Advanced Techniques

# a) Compiling Patterns
# Compiling a pattern allows for faster matching when used multiple times.

pattern = re.compile(r"\\d+")
matches = pattern.findall("There are 3 apples and 7 bananas")

# b) Flags in Regular Expressions
# Flags modify regex behavior, such as case sensitivity and multi-line matching.

# Flags:
# - re.IGNORECASE or re.I: Case-insensitive matching
# - re.MULTILINE or re.M: ^ and $ match start/end of each line
# - re.DOTALL or re.S: Dot (.) matches newlines

pattern = re.compile(r"hello", re.IGNORECASE)
 

 