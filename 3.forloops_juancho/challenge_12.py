import cmath 
print("Welcome to the Quadratic Equation Solver App")

print("A queadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real of complex numbers.")
print("A complex number has two parts : a +bj")
print("Where a is the real portion and bj is the imaginary portion.")
print("How many equations wouuld you like solve today: ")


equations = int(input())

for range in (0,equations):
    print("Solvin equation #1 ")
    print("Please enter your value of a (coefficent of x^2) :")
    a= float(input())
    print("Please enter your value of a (coefficent of x) :")
    b= float(input())
    print("Please enter your value of a (coefficent )")
    c = float(input())

    d = (b**2) - (4*a*c)

    x1 = (-b -cmath.sqrt(d))/(2*a)
    x2 = ((-b -cmath.sqrt(d))/(2*a))

    print(f"""
    The solution to {a}x^2 + {b}x + {c} = are:
    x1 = {x1}
    x2 = {x2}
    """)