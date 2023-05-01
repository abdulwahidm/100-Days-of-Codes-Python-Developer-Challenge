"""
The premiere of a computer game is planned and the option to subscribe to the wish list is opened. 
When a user subscribes to the wish list user id is added to the deque.
Several users subscribed to the wish list. The data is received as a stream. 
If an error occurs, the value None appears in the stream instead of the user id. 
In this case, the deque should be cleared.

Using the built-in collections module create an empty deque object named wishlist.
Following users subscribed to the wish list in the given order (in stream):

'003'
'001'
'004'

None

'002'
'005'

Add these users to the wishlist deque in the way described above. 
In response, print the wishlist to the console.

Tip:
>>> help(deque)
 
Help on class deque in module collections:
 
class deque(builtins.object)
 |  deque([iterable[, maxlen]]) --> deque object
 |  
 |  A list-like sequence optimized for data accesses near its endpoints.

Expected result:

deque(['002', '005'])
"""

from collections import deque
 
user_ids = ['003', '001', '004', None, '002', '005']
 
wishlist = deque()
for user_id in user_ids:
    if user_id is not None:
        wishlist.append(user_id)
    else:
        wishlist.clear()
 
print(wishlist)