"""
The following dictionary is given:

tesla = {
    'Close': {
        0: 1499.11,
        1: 1476.49,
        2: 1539.6,
        3: 1417.0,
        4: 1513.07,
        5: 1592.33,
        6: 1568.36,
        7: 1643.0,
        8: 1500.84,
        9: 1500.64,
    },
    'Date': {
        0: '2020-07-29',
        1: '2020-07-28',
        2: '2020-07-27',
        3: '2020-07-24',
        4: '2020-07-23',
        5: '2020-07-22',
        6: '2020-07-21',
        7: '2020-07-20',
        8: '2020-07-17',
        9: '2020-07-16',
    },
    'Volume': {
        0: 9426893,
        1: 15808700,
        2: 16048669,
        3: 19396616,
        4: 24328504,
        5: 14161080,
        6: 16157280,
        7: 17121367,
        8: 9329972,
        9: 14300785,
    },
}


Using the built-in itertools module and the takewhile class create an iterator 
to iterate through the closing prices from the tesla dictionary (the Close key) 
until a price greater than 1600 is found and assign to the results variable.

In response, print all elements of the results iterator to the console as shown below.

Tip:
>>> help(itertools.takewhile)
Help on class takewhile in module itertools:
 
class takewhile(builtins.object)
 |  takewhile(predicate, iterable, /)
 |  
 |  Return successive entries 
 from an iterable as long as the predicate evaluates to true for each entry.

Expected result:

1499.11
1476.49
1539.6
1417.0
1513.07
1592.33
1568.36
"""

import itertools
 
tesla = {
    'Close': {
        0: 1499.11,
        1: 1476.49,
        2: 1539.6,
        3: 1417.0,
        4: 1513.07,
        5: 1592.33,
        6: 1568.36,
        7: 1643.0,
        8: 1500.84,
        9: 1500.64,
    },
    'Date': {
        0: '2020-07-29',
        1: '2020-07-28',
        2: '2020-07-27',
        3: '2020-07-24',
        4: '2020-07-23',
        5: '2020-07-22',
        6: '2020-07-21',
        7: '2020-07-20',
        8: '2020-07-17',
        9: '2020-07-16',
    },
    'Volume': {
        0: 9426893,
        1: 15808700,
        2: 16048669,
        3: 19396616,
        4: 24328504,
        5: 14161080,
        6: 16157280,
        7: 17121367,
        8: 9329972,
        9: 14300785,
    },
}

results = itertools.takewhile(
    lambda price: price <= 1600, tesla['Close'].values()
)

for result in results:
    print(result)