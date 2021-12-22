from datetime import datetime
# usamos la función 

shoppingList = ['Meat','Cheese']
print('Bienvenido a la lista de la compra')

print('Son las : '+str(datetime.now()))

print('Usted a añadido '+ str(shoppingList[0])+' Y '+str(shoppingList[1])+' En su lista\n')

# cambiamos los valores a nuestra nueva lista
for i in range(3):
    shoppingList.append(str(input('Que tipo de comida le gustaria añadir a la lista: ')))

print('\nAqui tenemos los valores de la lista: '+str(shoppingList))
shoppingList.sort()
print('Aqui tenemos la lista Ordenada ')

print('\nSimulando la compra\n')
# borramos los valores de la lista
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i].capitalize()

for i in range(3):
    print('Tu lista actual es: '+str(len(shoppingList))+' items\n'+str(shoppingList))
    food = str(input('Que comida acabas de comprar: '))
    print('Eliminando '+food+' De la lista...')
    shoppingList.remove(food.capitalize())

print('\nTu lista actual es: '+str(len(shoppingList))+' items\n'+str(shoppingList))

#eliminamos 

print('Lo sentimos no tenemos suministro de '+str(shoppingList[len(shoppingList)-1])+'.\n')
del(shoppingList[len(shoppingList)-1])
food = str(input('Que producto le gustaria : ')).capitalize()
shoppingList.append(food)
print('Aqui tenemos su lista actual : '+str(shoppingList))