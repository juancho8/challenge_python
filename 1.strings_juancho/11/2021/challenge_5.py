print("Welcome to the multiplication/exponent table App")
name = input("\nWhat is your name").title()
number = float(input("\nwhat number would you like to work with  : "))

print(f"\nMultiplication table for {number}")
print(f""" 1.0*{number} = {number * 1}
           2.0*{number} = {number * 2}
           3.0*{number} = {number * 3}
           4.0*{number} = {number * 4}
           5.0*{number} = {number * 5}
           6.0*{number} = {number * 6}
           7.0*{number} = {number * 7}
           8.0*{number} = {number * 8}
           9.0*{number} = {number * 9}""")
print(f""" now we will elevate to
           1.0**{number} = {number ** 1}
           2.0**{number} = {number ** 2}
           3.0**{number} = {number ** 3}
           4.0**{number} = {number ** 4}
           5.0**{number} = {number ** 5}
           6.0**{number} = {number ** 6}
           7.0**{number} = {number ** 7}
           8.0**{number} = {number ** 8}
           9.0**{number} = {number ** 9}""")
print(f'{name} math is cool.')
