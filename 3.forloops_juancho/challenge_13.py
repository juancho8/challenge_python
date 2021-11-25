print("Welcome to the Facotiral Calculator App")
print("What number would you like to compute the factorial of ?")


n = int(input("Enter a number: "))

a = 1
for i in range(2, n + 1):
 a *= i
print(f"Here is the result form the math library: {a}")

print(f"Here is the result form my own algorithm:{a}")
