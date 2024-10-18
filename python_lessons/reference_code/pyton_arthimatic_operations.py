# Python Arithmetic Operations Example

# 1. Addition (+)
num1 = 10
num2 = 5
result_add = num1 + num2
print(f"Addition: {num1} + {num2} = {result_add}")

# 2. Subtraction (-)
result_sub = num1 - num2
print(f"Subtraction: {num1} - {num2} = {result_sub}")

# 3. Multiplication (*)
result_mul = num1 * num2
print(f"Multiplication: {num1} * {num2} = {result_mul}")

# 4. Division (/)
result_div = num1 / num2
print(f"Division: {num1} / {num2} = {result_div}")

# 5. Modulus (%): Returns the remainder of the division
result_mod = num1 % num2
print(f"Modulus: {num1} % {num2} = {result_mod}")

# 6. Exponentiation (**): Raises one number to the power of another
result_exp = num1 ** num2
print(f"Exponentiation: {num1} ** {num2} = {result_exp}")

# 7. Floor Division (//): Divides and returns the largest whole number less than or equal to the result
result_floor_div = num1 // num2
print(f"Floor Division: {num1} // {num2} = {result_floor_div}")

# 8. Combined Operations
combined_result = (num1 + 2) * (num2 - 1) / 2
print(f"Combined Operations: (10 + 2) * (5 - 1) / 2 = {combined_result}")

# 9. Order of Operations (PEMDAS): Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
order_of_operations_result = 3 + 5 * 2 ** 2 / 2 - 1
print(f"Order of Operations Result: 3 + 5 * 2 ** 2 / 2 - 1 = {order_of_operations_result}")

# 10. Arithmetic with negative numbers
negative_num1 = -7
negative_num2 = -3

result_neg_add = negative_num1 + negative_num2
result_neg_mul = negative_num1 * negative_num2
print(f"Negative Addition: {negative_num1} + {negative_num2} = {result_neg_add}")
print(f"Negative Multiplication: {negative_num1} * {negative_num2} = {result_neg_mul}")
