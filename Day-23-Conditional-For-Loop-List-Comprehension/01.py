"""
Write a program that creates a histogram as a dictionary of the following values:

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

In response print histogram to the console.

Expected result:

{'x': 3, 'y': 4, 'z': 2}

"""

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
freq = {}
 
for item in items:
    if item not in freq.keys():
        freq[item] = 1
    else:
        freq[item] += 1
 
 
print(freq)
