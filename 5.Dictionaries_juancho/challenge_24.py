from collections import Counter

# usamos la biblioteca collections para poder usar la funcion counter 


print("\tWelcome to the Frequency Analysis App")

non_letters = ["1","2","3","4","5","6","7","8","9","0"," ",",",".","?","\n","\t","!",'"','$','-','@',';',"'"]

# la lista es para conterner todos los posibles valores 

for i in range(1,3):
    # El bucle contendra los valors del 1 al 3 y se va a ir revitaliznado  


    key_phrase_1 = input("\nEnter a word or phrase to count the occurrence of each letter: ").lower()
    print("\nHere is the frequency analysis from key phrase ",i,":")
    new_phrase = ''.join( i for i in key_phrase_1 if i not in non_letters) 

    # esta es la parte logica clave .join crea una lista y divide los valores de la lista con comas 

    total_ocurrences = len(new_phrase)
    letter_count = Counter(new_phrase)
    lista = []

    print("\n\tLetter\t\tOcurrence\t\tPercentage")
    for clave,valor in sorted(letter_count.items()):


        print("\t",clave,"\t\t",valor,"\t\t",round(valor/total_ocurrences *100,2))
    order_letter_count = letter_count.most_common()

    for i in range(len(order_letter_count)):

        for j in range(0,1):
            lista.append(order_letter_count[i][j])
    lista = "".join(lista)
    print("\nLetters ordered from highest occurrence to lowest:")
    print(lista)