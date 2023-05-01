"""
The Phone class and the __init __() method are defined below:

class Phone:
    def __init__(self, price):
        self.price = price 

When creating a Phone class instance, we set the price attribute without any validation. 
This can raise some problems. For example, we can set a text value as a price:

phone = Phone('Apple')
or a negative value:
phone = Phone(-10)

Which is not necessarily what we want.

Correct the implementation of the __init __() method to verify if the value is a positive number 
before setting the price attribute. Use the built-in numbers module for this. 
If the value isn't a positive number, raise the TypeError with the following message:

Parameter 'value' must be a positive number.
"""

import numbers
 
class Phone:
 
    def __init__(self, price):
        if isinstance(price, numbers.Number) and price > 0:
            self.price = price
        else:
            raise TypeError(
                "Parameter 'value' must be a positive number."
            )
        

nokia = Phone(89)
samsung = Phone("galaxy")

print(nokia.price)