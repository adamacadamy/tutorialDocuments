
# Lesson: Reading and Writing to Files in Python

# 1. Opening a File
# To open a file, use the open() function. Specify the file name and the mode ('r' for read, 'w' for write, 'a' for append).
# After working with the file, you should close it to free system resources.

file = open('example.txt', 'r')  # Open a file in read mode
file.close()  # Always close the file after using it

# 2. Reading from a File
# You can read the entire content of a file using the read() method, or read it line by line using a loop or the readlines() method.

# Reading the entire content
file = open('example.txt', 'r')
content = file.read()  # Read the file content
print(content)  # Print the content
file.close()  # Close the file

# Reading line by line
file = open('example.txt', 'r')
for line in file:
    print(line.strip())  # Print each line, removing extra newlines with strip()
file.close()  # Close the file

# Reading lines as a list
file = open('example.txt', 'r')
lines = file.readlines()  # Read all lines into a list
print(lines)  # Print the list of lines
file.close()  # Close the file

# 3. Writing to a File
# To write data to a file, you need to open it in 'w' (write) or 'a' (append) mode. 
# Writing to a file will overwrite the file if it exists (in 'w' mode).

# Writing a single string
file = open('output.txt', 'w')  # Open a file in write mode
file.write("Hello, this is a line of text.")  # Write a string to the file
file.close()  # Close the file

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file = open('output.txt', 'w')  # Open the file in write mode
file.writelines(lines)  # Write a list of lines to the file
file.close()  # Close the file

# 4. Using the 'with' Statement (Context Manager)
# Using 'with' to handle file operations is preferred because it automatically closes the file after the block of code is executed.

with open('example.txt', 'r') as file:
    content = file.read()  # Read the content of the file
    print(content)  # Print the content

# Writing with 'with' statement
with open('output.txt', 'w') as file:
    file.write("Writing with context manager ensures the file is closed properly.")

# 5. Reading and Writing Binary Files
# When working with non-text files, like images or audio files, use binary mode ('rb' for reading, 'wb' for writing).

# Reading a binary file
with open('image.png', 'rb') as file:
    binary_data = file.read()  # Read the binary data

# Writing binary data
with open('copy_image.png', 'wb') as file:
    file.write(binary_data)  # Write the binary data to a new file

# 6. Common File Methods
# file.read(size): Reads the specified number of characters or bytes from the file.
# file.readline(): Reads a single line from the file.
# file.readlines(): Reads all the lines and returns them as a list.
# file.write(string): Writes the string to the file.
# file.writelines(list_of_strings): Writes multiple lines to the file.
