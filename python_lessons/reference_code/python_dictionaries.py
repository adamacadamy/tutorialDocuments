# Dictionary operations in Python with examples

# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Original dictionary:", my_dict)

# Accessing values using keys
name = my_dict["name"]
print("Accessed value for key 'name':", name)

# Using get() to access values (returns None if the key is not found)
age = my_dict.get("age")
print("Accessed value using get('age'):", age)
non_existent = my_dict.get("address")
print("Accessed non-existent key using get('address'):", non_existent)

# Adding a new key-value pair
my_dict["email"] = "john@example.com"
print("After adding new key 'email':", my_dict)

# Updating a value
my_dict["age"] = 31
print("After updating value for key 'age':", my_dict)

# update(): Updates multiple key-value pairs
my_dict.update({"city": "San Francisco", "phone": "123-456-7890"})
print("After update({'city': 'San Francisco', 'phone': '123-456-7890'}):", my_dict)

# remove(): Removes a specific key-value pair using pop(), returns the value
removed_value = my_dict.pop("phone")
print(f"After pop('phone'), removed value: {removed_value}, dictionary now:", my_dict)

# popitem(): Removes and returns the last inserted key-value pair (since Python 3.7)
last_item = my_dict.popitem()
print(f"After popitem(), removed item: {last_item}, dictionary now:", my_dict)

# del: Deletes a specific key-value pair
del my_dict["email"]
print("After del my_dict['email']:", my_dict)

# clear(): Removes all key-value pairs from the dictionary
my_dict.clear()
print("After clear(), dictionary:", my_dict)

# Re-creating dictionary for more examples
my_dict = {
    "name": "John",
    "age": 31,
    "city": "San Francisco"
}

# keys(): Returns a view of all the keys in the dictionary
keys = my_dict.keys()
print("Keys of the dictionary:", keys)

# values(): Returns a view of all the values in the dictionary
values = my_dict.values()
print("Values of the dictionary:", values)

# items(): Returns a view of all the key-value pairs in the dictionary
items = my_dict.items()
print("Items of the dictionary:", items)

# Using in to check if a key exists in the dictionary
is_name_in_dict = "name" in my_dict
print("Is 'name' a key in my_dict:", is_name_in_dict)

# Iterating through a dictionary
print("Iterating through the dictionary (keys):")
for key in my_dict:
    print(key, ":", my_dict[key])

print("Iterating through the dictionary (items):")
for key, value in my_dict.items():
    print(key, ":", value)

# Copying a dictionary using copy()
my_dict_copy = my_dict.copy()
print("Copied dictionary:", my_dict_copy)

# Nested dictionary example
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print("Nested dictionary:", nested_dict)

# Accessing nested dictionary values
