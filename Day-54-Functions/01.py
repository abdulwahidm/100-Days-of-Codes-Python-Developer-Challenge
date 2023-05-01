"""
For any:

we define the Euclidean distance by the formula:

Implement a function called euclidean_distance() that computes the distance between two points.

Example:

[IN]: euclidean_distance([0, 3], [4, 0])
[OUT]: 5.0

Note: You only need to implement this function.
"""

def euclidean_distance(x, y):
    squared_diff = [(i - j)**2 for i, j in zip(x, y)]
    return (sum(squared_diff)) ** 0.5

point_01 = [0, 3]
point_02 = [4, 0]

print(euclidean_distance(point_01, point_02))