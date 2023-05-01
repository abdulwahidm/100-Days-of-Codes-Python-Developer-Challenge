"""

Read the currencies.txt file. Each line has a different currency pair. 
Create a list with the names of currency pairs containing the 'USD' symbol.

Expected result:

['ARSUSD', 'AUDUSD']

"""

with open('currencies.txt', 'r') as file:
     lines = file.read().splitlines()
 
indexes = [index for index in lines if 'USD' in index]
 
print(indexes)