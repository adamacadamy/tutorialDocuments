# Python Logical Operations Example

# Logical AND (and): Returns True if both conditions are True
x = 10
y = 5
result_and = (x > 5) and (y < 10)
print(f"Logical AND: (x > 5) and (y < 10) = {result_and}")

# Logical OR (or): Returns True if at least one condition is True
result_or = (x < 5) or (y < 10)
print(f"Logical OR: (x < 5) or (y < 10) = {result_or}")

# Logical NOT (not): Reverses the result, True becomes False, False becomes True
result_not = not (x < 5)
print(f"Logical NOT: not (x < 5) = {result_not}")

# Combining multiple logical operations
combined_logical = (x > 5) and (y < 10) or (x == y)
print(f"Combined Logical: (x > 5) and (y < 10) or (x == y) = {combined_logical}")

# Comparison Operators

# Greater than (>)
result_gt = x > y
print(f"Greater than: x > y = {result_gt}")

# Less than (<)
result_lt = x < y
print(f"Less than: x < y = {result_lt}")

# Equal to (==)
result_eq = x == y
print(f"Equal to: x == y = {result_eq}")

# Not equal to (!=)
result_ne = x != y
print(f"Not equal to: x != y = {result_ne}")

# Greater than or equal to (>=)
result_ge = x >= y
print(f"Greater than or equal to: x >= y = {result_ge}")

# Less than or equal to (<=)
result_le = x <= y
print(f"Less than or equal to: x <= y = {result_le}")

# Logical operations with comparison results

# Check if a number is within a range using AND
is_within_range = (x > 5) and (x < 15)
print(f"Is {x} within range 5 and 15: {is_within_range}")

# Check if a number is outside a range using OR
is_outside_range = (x < 5) or (x > 15)
print(f"Is {x} outside range 5 and 15: {is_outside_range}")

# Negating a condition using NOT
not_in_range = not (x > 5 and x < 15)
print(f"Not in range 5 and 15: {not_in_range}")

# Logical operation with Boolean values
a = True
b = False
bool_and = a and b
bool_or = a or b
bool_not = not a
print(f"Boolean AND: a and b = {bool_and}")
print(f"Boolean OR: a or b = {bool_or}")
print(f"Boolean NOT: not a = {bool_not}")

# Combining logical and comparison operators
num = 20
is_even_and_positive = (num % 2 == 0) and (num > 0)
print(f"Is {num} even and positive: {is_even_and_positive}")

is_odd_or_negative = (num % 2 != 0) or (num < 0)
print(f"Is {num} odd or negative: {is_odd_or_negative}")
