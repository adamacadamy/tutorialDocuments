""" 
 address = "12, Berlin, 6232 , afdsasf, "
A regular expression is a special sequence of characters that help
you match or find other strings or sub set string etc...

# The main functions provided by the re module are:
# - re.match(): checks for a match only at the beginning of the string.
# - re.search(): searches for a match anywhere in the string.
# - re.findall(): returns a list of all non-overlapping matches in the string.
# - re.sub(): replaces matches with a new string.
# - re.split(): splits a string by the occurrences of a pattern."""

import re

# Special Characters
# . matches any character except a new line [ any except new line `\n`]
# ^ matches at the beginning of a string  
# $ match at the end of a string
# * matches 0 or more time [0 or many ] None   azasdfasdfa
# + matches 1 or more times [1 or many] azasdfasdfa
# ? matches 0 or 1 repetition [ axaxa]
# {} matches the number of repetition  a{4} aasdfasdfa
# [] matches any single character found with in the square brackets [acb]  aje3acdb
# | or 
# \\ escape special characters
# \d means digit
# \w word
# \s space or sentence
text = "Hello World"

pattern = r"Hello"
match = re.search(pattern, text)
print(match)

pattern = r"^Hello" # "Hello"  ዝብል ኣሎ ድዩ
match = re.search(pattern, text)
print(match)

text = "123abc"
pattern = r"\d+" # ሓደ ወይ ልዕሊ ሓደ ቁጽሪ ኣሎ ድዩ
match = re.search(pattern, text)
print(match)

pattern = r"\d{3}" # ኣብዚ ጽሑፍ ኣሃዛት ልዕሊ 3 ግዜ ተደጊሞም ኣለዉ ድዮም
match = re.search(pattern, text)
print(match)
print("----------search----------------")
pattern = r"[a-zA-Z]"
match = re.search(pattern, text)
print(match)


print("----------findall----------------")
text = "Hello World"
pattern = r"[a-z]"
result = re.findall(pattern, text)
print(result)

""" 
() group
(\w+) = word one or more times
\s = space 
(\w+) = word one or more times
, = exactly comma
age= exactly word `age`
(\d+)= digit one or more

putting all together
group of one or more words followed by space
and then followed by one or more words and 
then followed by comma and then followed by
space and then followed by
exactly word `age` as a group and then followed space
and the followed one or more digits

"""

text = "John Doe, age 30"
pattern = r"(\w+)\s(\w+),\s(age)\s(\d+)"
match = re.search(pattern, text)
print(match)

if match:
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group(4))
    
pattern = r"(?P<first_name>\w+)\s(?P<last_name>\w+)"
match = re.search(pattern, text)

print("named groups")
print(match)
if match:
    print(match.group("first_name"))
    print(match.group("last_name"))

result = re.search(r"John(?= Doe)", "John Doe")

print(result)
email = "someone@yahoo.com"
pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
matches = re.match(pattern, email)

print(matches)



text = "apple, banana; grape|orange"
# text.split()
# ['apple,', 'banana;', 'grape|orange']
pattern = r"[,;|]"
""" 
"apple, banana; grape|orange"
["apple", " banana; grape|orange"]
["apple", ["banana", grape|orange"]]
["apple", ["banana", [grape","orange"]]]
flattens the  nd list
["apple", "banana", grape","orange"]

"""
result = re.split(pattern, text)

print(result)
# ['apple', ' banana', ' grape', 'orange']

text = "The rain in spain"

pattern=r"rain"
new_text = re.sub(pattern, "sun", text)
print(new_text)

text="There are 3 apples and 7 bananas"
pattern = re.compile(r"\d+")
matches = pattern.findall(text)
print(matches)