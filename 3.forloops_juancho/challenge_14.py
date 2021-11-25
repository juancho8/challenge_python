print("Welcome to the Fibbonacci Calculator App")
print("How many digits of the Fibonacci Sequence would you like to computer: ")
n = int(input())
a = 0 
b = 1
sum = 0 
count = 1

while (count<= n):
  print( sum,end = "")
  # el comando end  ( va a hacer print de la suma y terminar con un espacio)
  # es un parametro de print
  count += 1
  a = b
  b = sum 
  sum = a +b

