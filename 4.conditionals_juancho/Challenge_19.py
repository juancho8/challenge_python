
import random

# una vez mas libreria random nos sirve para acceder a un numero aleatorio 

print("\tWelcome to the Guess My Number App")
name = input("\nHello! What is your name: ").title()

# el usuario debe adivinar el numero 

print("Well ",name,", I am thinking of a number between 1 and 20.")
x = random.randint(1,20)

#Aqui usamos las condicionales por si el usuario acierto o no
for i in range(1,7):
    num= int(input("\nTake a guess: "))
    if num < x:
        print("Your guess is too low.\n")

    #operadores de comparacion para saber si es correcta la sugestion

    elif num > x:
        print("Your guess is too high.\n")
        
    elif num == x:
        print("\nGood job, ",name,"! You guessed my number in ",i," guesses!")
        break
    if i == 5 :
        print("\nGame Over. The number I was thinking of was ",x,".")
        break