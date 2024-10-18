""" 
 loops, iterations
 are done for for flow related variables such as list, dict and etc
  1. while
  2. for

"""


# i=0
# # looping in ascending order :: from lesser value to greater value
# while i < 10: <= logical control
#     print(f"element {i}")
#     # i = i + 1 <= incremental control
#     i +=1 <= incremental control

""" 
 the flow is controlled by two syntactic mechanisms
  1. logical control
  2. incremental/decremental control
"""
# i = 9

# while i > -1: # <= logical control
#     print(f"element {i}")
#     # i = i - 1
#     i -=1   # <= arm control

# for i in range(0, 11, 1):
#     print(f"element {i}")
"""
arguments of range 
start, stop, increment or decrement
start = 0
stop = ?
i/d= 1


"""
# for i in range(10): # range(0, 10, 1)
#     print(f"element {i}")


my_list = [23, 1,22,19]

# print(my_list[2])
# my_list.sort(reverse=True)
"""
  loops:
    while |
          | logical control, arm control 
    for   |

"""
# for i in range(0, 4, 1):
#     print(f"element {my_list[i]} ")

# for i in range(0, len(my_list), 1):
#     print(f"element {my_list[i]} ")
    
# for element in my_list:
#     print(f" element {element}")

# my_set = {23, 1,22,19}

# my_set_list = list(my_set)

# my_set_list.remove(22)
# # my_set.pop()
# # my_set.remove(22)

# print(my_set)


my_dict = {
    "name": "adam",
    "age": 25,
    "city": "Gross Gerau"
}

""" 
keys and values

keys = ["name", "age", "city"]
values = ["adam", 25, "Gross Gerau"]

"""
# keys = list(my_dict.keys())

# print(keys)

# values = list(my_dict.values())

# print(values)
# x, y = 1, 2
# my_nums = (1, 2)
# x, y = my_nums

# print(my_nums)
# print(x, y)
""" 
keys = ["name", "age", "city"]
values = ["adam", 25, "Gross Gerau"]

zipped = [ ("name","adam",), ("age",25,), ("city", "Gross Gerau")]
""" 
keys = list(my_dict.keys())
values = list(my_dict.values())

# for key, value in zip(keys, values):
#     print(key, value)
#     print(f"{key}  :  {value}")
    
# zipped = zip(keys, values)

# for key, value in zipped:
#     print(key, value)
#     print(f"{key}  :  {value}")
    
for key, value in my_dict.items():
    print(key, value)
    print(f"{key} : {value}")
    
    