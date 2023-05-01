"""
Consider the continuous capitalization model of interest. 
The future value in this model can be calculated as follows:

where:
FV - future value - the future value of investments
PV - present value - present value of the investment
e - Euler's number
r - interest rate (annual)
n - number of years

Using the built-in math module calculate the future value of $ 1,000 
in the model of continuous interest capitalization 
and the annual interest rate of 4% after 3 years.

In response, print the result to the console as shown below.

Expected result:

fv = $ 1127.50
"""

import math
 
pv = 1000
r = 0.04
n = 3
 
fv = pv * math.e ** (r * n)
 
 
print(f'fv = $ {fv:.2f}')