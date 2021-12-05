

import random
# una vez mas importamos la libreria para poder obtener un resultado aleatorio

print("\tWelcome to a game of Rock, Paper, Scissors")
# inicio al programa 

n = int(input("\nHow many rounds would you like to play: "))
player = 0
pc = 0

# funcio para escoger entre piedra papel y tijera 

x = random.choice(["rock","paper","scissors"])
#Empezamos el bucle for para que asi se jueguen la cantidad de rounds que el usuario escogió


for i in range(1,n+1):
    print("\nRound ",i)

    print("Player: ",player,"\tComputer: ",pc)
    m = input("Time to pick...rock, paper, scissors: ")
    print("\tComputer: ",x)
    print("\tPlayer: ",m)

    # creamos el bucle de comparacion para generar un ganador necesitamos 
    # generar  los operadores de comparacion suficientes para contener todas las opciones 
    if m == 'paper' and x == 'rock':
        player+=1
        print("\tPaper covers rock!")
        print("\tYou win round ",i)
    elif m == 'paper' and x== 'scissors':
        pc +=1
        print("\tScissors cuts paper!")
        print("\tComputer win round ",i)
    elif m == 'rock' and x== 'scissors':
        player +=1
        print("\tRock breaks scissors!")
        print("\tYou win round ",i)
    elif m == 'rock' and x == 'paper':
        pc +=1
        print("\tPaper covers rock!")
        print("\tComputer win round ",i)
    elif m == 'scissors' and x == 'paper':
        player +=1
        print("\tScissors cuts paper!")
        print("\tYou win round ",i)
    elif m == 'scissors' and x== 'rock':
        pc +=1
        print("\tRock breaks scissors!")
        print("\tComputer win round ",i)
    elif m == x:
        player = player
        pc = pc
        print("\tIt is a tie, how boring!")
        print("\tThis round was a tie.")



print("\nFinal Game Results")
# se vana imprimir los resultados finales 
print("\tRound played: ",n)
print("\tPlayer score: ",player)
print("\tComputer score: ",pc)
# necesitamos otro comparador para mostrar de manera externa la operacion que a hecho nuestro anterior  if y elifs correspondientes
if player > pc:
    print("\tWINNER: PLAYER!!!")
elif pc > player:
    print("\tWINNER: COMPUTER :-(")
elif pc == player:
    print("\tWINNER: nobody, it's a tie")
