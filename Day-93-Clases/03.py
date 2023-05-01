"""A class called Laptop was implemented. Then, an instance of the Laptop 
class named laptop was created with the following arguments:
'Acer'
'Predator'
5490

In response, print the value for each instance attribute 
(on a separate line) of the laptop instance as shown below.

Expected result:
brand -> Acer
model -> Predator
price -> 5490
"""

class Laptop:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


laptop = Laptop('Acer', 'Predator', 5490)

print(f'brand -> {laptop.brand}')
print(f'model -> {laptop.model}')
print(f'price -> {laptop.price}')