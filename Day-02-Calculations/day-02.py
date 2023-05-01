"""
@ Exercise 1
Write a program that calculates the delta for quadratic equation:
    3x^2 - 4x + 1 = 0
Print the result to the console as shown below.
Expected result:
    Delta: 4
"""

# a = 3
# b = -4
# c = 1

# delta = b**2 - 4 * a * c
# print(f'Delta: {delta}')


""" 
@ Exercise 2 
The arithmetic sequence is given with the following formula: 
    an = 10 + 10n

Calculate the sum of the first ten elements of this sequence. 
Print the result to the console as shown bellow. Expected result: 
    The sum of the first 10 elements in a sequence: 320.0 bisa menggunakan semua hal yang perm
"""

# a1 = 14
# a10 = 50
# n = 10
 
# s10 = ((a1 + a10) / 2) * n
# print(f'The sum of the first 10 elements in a sequence: {int(s10)}')

""""
Exercise 3
The geometric sequence is given with the following formula:
    an = 8.2^(n-1)

Calculate the sum of the first six elements of this sequence. 
Print the result to the console as shown below. Expected result:
    The sum of the first 6 elements of the sequence is: 504.0
"""

a1 = 8
a2 = 8 * 2
n = 6
 
q = a2 / a1
s6 = a1 * ((1 - q**n) / (1 - q)) 
print(f'The sum of the first {n} elements of the sequence is: {int(s6)}')