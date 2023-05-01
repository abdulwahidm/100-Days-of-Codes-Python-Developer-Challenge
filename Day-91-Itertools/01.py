"""
The following list is given:

fnames = [
    '01_image.jpg',
    '02_image.png',
    '03_image.jpg',
    '04_image.jpg',
    '05_image.jpg',
    '06_image.png',
    '07_image.jpg',
    '08_image.png',
    '09_image.svg',
    '10_image.svg',
    '11_image.jpeg',
    '12_image.jpeg',
]

Using the built-in module itertools and the groupby class, 
group the names of the files by extension (properly sort the data before grouping). 
Use extensions as grouping keys.

In response, print the keys and the percentage share of the extension 
in the entire fnames list to the console as shown below.

Tip:
>>> help(itertools.groupby)
Help on class groupby in module itertools:
 
class groupby(builtins.object)
 |  groupby(iterable, key=None)
 |  
 |  make an iterator that returns consecutive keys and groups from the iterable
 |  
 |  iterable
 |    Elements to divide into groups according to the key function.
 |  key
 |    A function for computing the group category for each element.
 |    If the key function is not specified or is None, the element itself
 |    is used for grouping.


Expected result:
jpeg -> 16.67%
jpg -> 41.67%
png -> 25.0%
svg -> 16.67%
"""

import itertools

fnames = [
    '01_image.jpg',
    '02_image.png',
    '03_image.jpg',
    '04_image.jpg',
    '05_image.jpg',
    '06_image.png',
    '07_image.jpg',
    '08_image.png',
    '09_image.svg',
    '10_image.svg',
    '11_image.jpeg',
    '12_image.jpeg',
]

func = lambda fname: fname.split('.')[-1]
sorted_data = sorted(fnames, key=func)
# print(sorted_data)

grouped_data = itertools.groupby(sorted_data, key=func)

for key, group in grouped_data:
    print(
        f'{key} -> {round(100 * len(list(group))/ len(fnames), 2)}%'
    )