print("\tWelcome to the Even Odd Number Sorter App")

d = True # lo creamos para poder cerrar el bucle d 

while d :
    


    nums= input("Enter in a string of numbers separated by a comma (,): ")
    #Eliminamos los espacios en blanco


    nums = nums.replace(" ","")
    # variable para cambiar valores de la lista 
    num_list = nums.split(",")
    # variable para dividir valores de la lista y poner strings en medio
    pares = []
    impares = []


    for i in num_list:
        #Si los numeros cumplen los siguientes condicionales seran agregados en sus respectivas listas
        if int(i)%2 == 0:
            pares.append(i)
        elif int(i)%2 != 0:
            impares.append(i)

    #Ordenamos las listas de menor a mayor


    pares = sorted(pares)
    impares = sorted(impares)       
    print("\n----Result Sumary----")

    #Mostramos en pantalla los numeros en orden y si es par o impar


    for i in num_list:
        if i in pares:
            print("\t",i," is odd!")
        elif i in impares:
            print("\t",i," is even!")
    print("\nThe following ",len(pares)," numbers are odd:")

    # condicionales para impares y pares 
    for i in pares:
        print("\t",i)
    print("\nThe following ",len(impares)," numbers are even:")


    for i in impares:
        print("\t",i)
    c = input("Would you like to run the program again (y/n): ").lower()

    #condicinal para cerrar el bucle 
    
    if c == 'yes':
        continue
    elif c == 'no':
        print("Thank you for using the program. Goodbye.")
        d = False
