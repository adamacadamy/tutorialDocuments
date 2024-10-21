""" 
 list comprehension
 dict comprehension
 tuple comprehension

"""
list_of_10_numbers = []

for i in range(0, 10, 1):
    if i % 2 == 0:
        list_of_10_numbers.append(i)
    
print(list_of_10_numbers)

# with list comprehension
list_of_10_numbers = [ i for i in range(0, 10, 1) if i % 2 == 0] 

print(list_of_10_numbers)

list_of_sqr_10_numbers = [ i**2 for i in range(0, 10, 1)] 

print(list_of_sqr_10_numbers)

input_dict = {'apple': 1, 'banana': 5, 'orange': 3}

filtered_dict= { k: v for k, v in input_dict.items() if "n" in k}

print(filtered_dict)

dict_of_10_numbers = { str(i):i for i in range(0, 10, 1)}

print(dict_of_10_numbers)

