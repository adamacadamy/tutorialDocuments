""" 
flow control
  when you want to incrementally execute or operate  you
  can you flow control
"""

""""
i = 0

first iteration 1ይ ዙርያ
 i = 0
 i+=1  => 1 since 0 + 1 = 1
 condition not met since i < 10 [ 1 < 10]
 
second iteration 2ይ ዙርያ
 i = 1
 i+=1  => 1 since 1 + 1 = 2
 condition not met since i < 10 [ 2 < 10]
 
second iteration
 i = 2
 i+=1  => 1 since 2 + 1 = 3
 condition not met since i < 10 [ 3 < 10]
 
 ..
....

eighth iteration
 i = 7
 i+=1  => 1 since 7 + 1 = 8
 condition not met since i < 10 [ 8 < 10]
 
 
ninth iteration
 i = 8
 i+=1  => 1 since 8 + 1 = 9
 condition not met since i < 10 [ 9 < 10]
 
 
 
tenth iteration 10ይ ዙርያ
 i = 9
 i+=1  => 1 since 9 + 1 = 10
 condition  met since i == 10 [ 10 < 10] then break the loop
  


"""
# while loop
# i = 0
# while i < 10: # condition
#     print(i)
#     # i+=1
#     i=i+1

"""
i = 10 initially

first loop:
    i = 10
    i-=1 => 9
 condition not met since > -1 [ 10 > -1] then break the loop

second loop:
    i = 9
    i-=1 => 8
 condition not met since > -1 [ 9 > -1] then break the loop

second loop:
    i = 9
    i-=1 => 7
 condition not met since > -1 [ 7 > -1] then break the loop


...

tenth loop:
    i = 0
    i-=1 => -1
 condition  met since > -1 [ -1 > -1] then break the loop



"""
# i = 10

# while i > -1:
#     print(i)
#     i=i-1

print("---------------------------------------------------------------------------------------")

"""
range will generate a list of 10 elements
and i will represent one element from the loop during each iteration
 
 range(10) => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
fist iteration:
 i = 0

second iteration:
  i = 1
  
third iteration:
    i = 2
...
...
eighth iteration:
  i = 7

ninth iteration:
  i = 8

tenth iteration:
  i = 10
  

"""
# # for loop
# for i in range(10): # list = [0, ..., 9]
#     print(i)
    
    
print("---------------------------------------------------------------------------------------")

# range built in function is to be supplied by three arguments
# 1. starting of the iteration
# 2. end of iteration
# 4. step
"""
 starting point = 3
 ending point = 6
 jump value/ increment value = 1
 
 first iteration:
     i = 3

 second iteration:
     i = 4
     
 third iteration:
    i = 5
    
    
 
#  """
# for i in range(3, 6, 1):
#     print(i)
    
    
for i in range(10):
    print(i)