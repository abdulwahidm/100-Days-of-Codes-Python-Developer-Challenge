"""
Implement a function map_longest() that accepts the list of words 
and return the length of the longest word in this list.

Example:

[IN]: map_longest(['python', 'sql'])
[OUT]: 6

[IN]: map_longest(['java', 'sql', 'r'])
[OUT]: 4


Note! You only need to define the function. 
"""

def map_longest(words):
    length = []
    for word in words:
        length.append(len(word))
    return max(length)

print(map_longest(['python', 'java']))
print(map_longest(['java', 'sql', 'r']))