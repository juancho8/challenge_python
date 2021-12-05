print("\tWelcome to the Factor Generator App")

c = True # para poder cerrar el bucle con un c = false

while c :
    # hemos creado un bucle en funcion de c con la intencion de poder cerrarlo desde dentro 


    num = int(input("\nEnter a number to determine all factors of that number: "))
    fact = []
    #Añadimos los factores del número


    for i in range(1,num+1):
        if num%i == 0:
            fact.append(i)
    print("\nFactors of ",num ," are:")
    #Mostramos los factores y la multiplicacion


    for i in fact:
        print(i)
    print("\nIn summary:")
    # mostramos el resumen


    for i in fact:
        for j in fact:
            if i*j==num and i<=j:
                print(i,"*",j," = ",num)
    s = input("Run again (y/n): ").lower()
    #obtenemos la respuesta del usuario para saber si quiere que vuelva a ser ejecutado


    if s == 'yes':
        continue
    if s == 'no':
        print("\nThank you for using the program. Have a great day.")
        break