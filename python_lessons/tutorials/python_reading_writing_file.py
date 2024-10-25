""" 
1. reading
2. writing
  atomic: 
    all steps happen in batch mode
"""

file = open('example.txt', 'w')
file.write(" HI I HAVE JUST BEEN WRITTEN")
file.close()

print("------------------------")
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

print("------------------------")

file = open('multiline.txt', 'w')
content = ["Line 1\n", "Line 2\n", "Line 3\n"]
file.writelines(content)
file.close()


print("------------------------")
file = open('multiline.txt', 'r')
content = file.readlines()
print(content)
file.close()


print("------------------------")
# atomic reading and atomic writing

with open('example_2.txt', 'w') as file:
    file.write(" some mambo jumbo")
    
    
print("------------------------")

with open('example_2.txt', 'r') as file:
    content = file.read()
    print(content)

    
print("------------------------")
# reading file as binary

with open("example_2.txt", 'rb') as file:
    binary_data = file.read()
    print(binary_data)
    
with open("example_2.txt", 'wb') as file:
    file.write(b' some mambo jumbo two')
