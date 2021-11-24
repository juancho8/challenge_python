import math
print("Welcome to the Right Triangle Solver App")
First_leg = int(input("What is the first leg of the triangle: "))
print(f"{First_leg}")
Second_leg = int(input("What is the Second leg of the triangle: "))
print(f"{Second_leg}")
hypotenuse = round(math.sqrt((First_leg**2)+(Second_leg**2)))

print(f"{hypotenuse}")
