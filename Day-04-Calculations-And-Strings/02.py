"""
From the following text:
string = 'PKV-89415-PLN'
extract the code containing the first three and last three characters. 
Print the result to the console.

Expected result:
    'PKVPLN'
"""

# Write Your Code Here
# ====================================================================================

string = 'PKV-89415-PLN'
code = string[:3] + string[-3:]  # concatenate the first three and last three characters
print(code)  # output: PKVPLN