# result = 1 / 0
x = input("Please enter the number \n")
y = int(x)
 

try:
    y = int(x)
    result = 1 / y
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
finally:
    print(""" 
          make sure to supply the right value an
          
          right order of division
          """)