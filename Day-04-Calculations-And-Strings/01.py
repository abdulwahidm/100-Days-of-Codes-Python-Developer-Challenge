"""
Calculate the geometric mean of the following numbers: 4, 3, 4.5, 5 
And print the result to the console as shown below.
Expected result:
    'Geometric average of the given numbers: 4.05'
"""

# Write your code here 
# ======================================================================== 

x1, x2, x3, x4 = 4, 3, 4.5, 5
# numbers = [4, 3, 4, 4.5, 5] 
geometric = (x1 * x2 * x3 * x4) ** (1/ 4)

print(f'Geometric average of the given numbers: {geometric:.2f}')

