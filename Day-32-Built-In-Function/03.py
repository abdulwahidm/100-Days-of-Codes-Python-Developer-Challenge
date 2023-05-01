"""
Count the number of ones in the binary representation of number:

number = 234

Print the result to the console.

Tip: Use the bin() built-in function.

Expected result:

5
"""

# ===================================================================
# your code here 

number = 234

binary = bin(number)
# print(bin(binary))

binary = binary[2:]
print(binary.count('1'))
