""" 
Exercise 1
Calculate the midpoint of the segment with ends at the points: A = (2,4) and B = (-4,6)
Print the result to the console as shown below. 
Expected result: 
    The middle point: (-1.0, 5.0)
"""

# Ax = 2
# Ay = 4
# Bx = -4
# By = 6
 
# x_midpoint = (Ax + Bx) / 2
# y_midpoint = (Ay + By) / 2
# print("The middle point: ({0:.1f}, {1:.1f})".format(x_midpoint, y_midpoint))

""" 
@ Exercise 2
Calculate the distance of two points A = (3, 2), B = (- 1, -1) 
and print result to the console as shown below.
Expected result: 
    The distance of A and B is 5.0
"""
 
Ax = 3; Bx = -1
Ay = 2; By = -1

distance = ((Bx - Ax)**2 + (By - Ay)**2  ) **(1/2)
print(f'The distance between point A and B: {distance}')


