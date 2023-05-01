"""
The results of voting in three groups are given in the form of dictionaries:

poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}
poll_3 = {'yes': 16, 'no': 14}

The dictionary keys mean respectively:

'yes' - vote for yes

'no' - vote for no

'None' - invalid vote

Using the built-in collections module and the Counter class find the total number of 'yes' votes and print to the console.

Tip:

>>> help(Counter)
 
Help on class Counter in module collections:
 
class Counter(builtins.dict)
 |  Dict subclass for counting hashable items.  Sometimes called a bag
 |  or multiset.  Elements are stored as dictionary keys and their counts
 |  are stored as dictionary values.

Expected result:

269
"""

from collections import Counter
 
poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}
poll_3 = {'yes': 16, 'no': 14}
 
cnt_1 = Counter(poll_1)
cnt_2 = Counter(poll_2)
cnt_3 = Counter(poll_3)
cnt_total = cnt_1 + cnt_2 + cnt_3
 
print(cnt_total['yes'])