from datetime import datetime, date
# importamos la funcion datetime para usala mas adelante :

shopping = ["meat", "cheese"]
new = input("Add three new items to the list separated by a coma: ")
new_items = new.split(", ")
shopping.extend(new_items)
# creamos la variable y despues metemos en la variable los 3 valores
#despues dividimos los valores separados con comags gracias al split

numero = input("Which item you just purchased? ")
shopping.remove(numero)

numero1 = input("Which item you just purchased? ")
shopping.remove(numero1)

numero2 = input("Which item you just purchased? ")
shopping.remove(numero,2)

new1 = input(f"Sorry, the store is out of {shopping.pop(1)}. Which other item would you like to purchase instead? ")
shopping.append(new1) 
#usamos pop para que se muestre en la pantalla

print(f"The final version of your grocery list looks like this: {shopping}")
print(f"\n{date.today().month}/{date.today().day} {datetime.today().hour}:{datetime.today().day}")