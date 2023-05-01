"""
Using the built-in collections module and the namedtuple() 
function create a class named Point to store points in a two-dimensional space (R^2). 
Name the fields 'x' and 'y' respectively.

Then create two points with coordinates:
(3, 4)
(-2, 6)

Print these objects to the console.

Tip:

>>> help(namedtuple)
Help on function namedtuple in module collections:
 
namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
    Returns a new subclass of tuple with named fields.

Expected result:

Point(x=3, y=4)
Point(x=-2, y=6)
"""

from collections import namedtuple
 
Point = namedtuple(typename='Point', field_names=['x', 'y'])
 
pt1 = Point(3, 4)
pt2 = Point(-2, 6)
 
print(pt1)
print(pt2)