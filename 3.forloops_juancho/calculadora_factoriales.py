# importamos la libreria para poder hacer operaciones
import math

print('BIENVENIDO A LA CALCULADORA DE FACTORIALES')
factorial = int(input('Que numero te gustaria utilizar : '))
result = 1
list = []

#Create the list of nums and calculate the factorial (My method)
for i in range(factorial,0,-1):
    list.append(i)
    if i == 1:
        list.reverse()
        list.insert(0,str(factorial)+'!')    
        list.insert(1,'=')  
    else:
        list.append('*')  
    result = result*i
print(*list)
#Math method
print('\nEste es el resultado de la libreria \nEl fatorial de  '+str(factorial)+' es: '+str(math.factorial(factorial)))

#My method
print('\nEste es el resultado del algoritmo \nEl factorial de  '+str(factorial)+' es: '+str(result))

print('\nSe muestra dos veces como '+str(factorial)+'! = '+str(result))   