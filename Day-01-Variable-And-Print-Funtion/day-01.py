#Print the Python version to the console
import sys
# print(sys.version.split()[0]) #3.10.6
print(sys.version.split()) #3.10.6



""" 
@ Exercise 1
Create two variables (you can freely choose the names) and 
assign to them following values:
    'Python'
    '3.8'
"""

# programming_language = "Python"
# version = "3.8"

# print('I love', programming_language, version + '!') # I love Python 3.8!

"""
@ Exercise 2
Assign two variables that store the following values:
    $ 42.99 - product price (float)
    30 lbs - product weight (int)

Using the f-string formatting style print to the console the following message:
    Price: $42.99. Weight: 30 lbs
"""
#============================================================================================================
# price = 42.99
# weight = 30

# print(f'Price: ${price}. Weight: {weight} lbs.')


"""
@ Exercise 3
Write a program that calculates the area of a circle with a radius = 10. Use an approximate value of pi:
    pi = 3.14

Print the result to the console as shown below. Expected result:
    Area: 314.00
"""

# pi = 3.14
# radius = 10
 
# area = pi * radius ** 2
# print(f'Area: {area:.2f}')

"""
@Exercise 4
Write a program that calculates the future value of 1000 USD with an annual interest rate of 3%, 
annual capitalization and a 5-year investment period. Round the result to the nearest cent.

Tip: Use compound capitalization of interest.
Print the result to the console as shown below.
Expected result:
    "The future value of the investment: 1159.27 USD"
"""

# pv = 1000
# r = 0.03
# n = 5
 
# fv = pv * (1 + r) ** n
# print(f'The future value of the investment: {fv:.2f} USD')

