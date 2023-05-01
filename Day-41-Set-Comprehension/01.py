"""
Consider the two-roll of the dice. 
Create the probability space (omega) 
and count the probability of getting a sum of points higher than 10. 
Use set comprehension.

Expected result:

Probability: 0.08

"""
Ω = {(i,j) for i in range(1,7) for j in range(1,7)}
A = {(i,j) for i in range(1,7) for j in range(1,7) if i+j > 10}
P_A = len(A) / len(Ω)
print(f"Probability:, {P_A:.2f}")

