# Python Control Flow Example Without Loops

x = 10

# if, elif, else statements

if x > 0:
    print(f"{x} is positive")
elif x == 0:
    print(f"{x} is zero")
else:
    print(f"{x} is negative")

# Nested if
y = 5
if y > 0:
    if y < 10:
        print(f"{y} is a positive number less than 10")
    else:
        print(f"{y} is a positive number greater than or equal to 10")
else:
    print(f"{y} is not a positive number")

# Using case/match statement (introduced in Python 3.10)

z = 2

match z:
    case 1:
        print("z is 1")
    case 2:
        print("z is 2")
    case 3:
        print("z is 3")
    case _:
        print("z is something else")

# Another example of match/case for string matching

fruit = "apple"

match fruit:
    case "apple":
        print("It's an apple!")
    case "banana":
        print("It's a banana!")
    case "orange":
        print("It's an orange!")
    case _:
        print("Unknown fruit")

# Ternary operator: Short form of if-else in one line
num = 8
result = "even" if num % 2 == 0 else "odd"
print(f"{num} is {result}")

# Example combining multiple conditional flows
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Case with different data types
value = (1, "a")

match value:
    case (1, "a"):
        print("Matched case: (1, 'a')")
    case (2, "b"):
        print("Matched case: (2, 'b')")
    case _:
        print("No match found")
