print('Welcome to the Favorite Teachers Program')

# obtenemos la lista con los profesores
Teachers = []
Teachers.append(str(input('quien es tu profesor favorito: ')).capitalize())
Teachers.append(str(input('quien es tu segundo profesor favorito: ')).capitalize())
Teachers.append(str(input('quien es tu tercer profesor favorito: ')).capitalize())
Teachers.append(str(input('quien es tu cuarto profesor favorito: ')).capitalize())

#mostramos los resultados
TeachersO = Teachers.copy() 
print('\nTus cuatro profesores favoritos : '+str(Teachers))
Teachers.sort()
print('Tus cuatro profesores favoritos ordenados alfabeticamente :'+str(Teachers))
Teachers.reverse()
print('Tus cuatro profesores favoritos ordenados alfabeticamente en orden inverso :'+str(Teachers))

print('\nTus dos profesores favoritos son : '+str(TeachersO[0])+ ' y '+str(TeachersO[1]))
print('Tus siguientes profesores favoritos: '+str(TeachersO[2])+ ' y '+str(TeachersO[3]))
print('El ultimo de tus profesores favoritos es : '+str(TeachersO[-1]))
print('Tienes un total de  '+str(len(TeachersO))+' Profesores favoritos\n')

#Cambiamos la posicion de los profesores
TeachersO.insert(0,str(input(('Oops, '+str(TeachersO[0])+' Ya no es tu profesor favorito,\n Quien es tu profesor favorito ')).capitalize()))

#limpiamos la primera lista con la funcion clear
Teachers.clear()
Teachers = TeachersO.copy()
print('\nTus profesores favoritos son: '+str(Teachers))
Teachers.sort()
print('Tus cuatro profesores favoritos ordenados alfabeticamente : '+str(Teachers))
Teachers.reverse()
print('Tus cuatro profesores favoritos ordenados alfabeticamente en orden inverso : '+str(Teachers))

# mostramos la informacion actualizada
print('\nTus dos profesores favoritos son: '+str(TeachersO[0])+ ' y '+str(TeachersO[1]))
print('Tus dos siguientes profesores favoritos son :'+str(TeachersO[2])+ ' y '+str(TeachersO[3]))
print('Tu ultimo profesor favorito es : '+str(TeachersO[-1]))
print('tienes un total de  '+str(len(TeachersO))+' Profesores favoritos\n')

#Eliminamos a un profesor
delProf = str(input('Ya no es tu profesor favorito,\n Quien es tu profesor favorito ')).capitalize()
TeachersO.remove(delProf)

#Limpiamos la anterior lista y renovamos
Teachers.clear()
Teachers = TeachersO.copy()
print('\nTus profesores favoritos son  '+str(Teachers))
Teachers.sort()
print('Tus cuatro profesores favoritos ordenados alfabeticamente :'+str(Teachers))
Teachers.reverse()
print('Tus cuatro profesores favoritos ordenados alfabeticamente en orden inverso :  '+str(Teachers))

#Mostramos los valores de los profesores en la lista final
print('\nTus dos profesores favoritos son: '+str(TeachersO[0])+ ' and '+str(TeachersO[1]))
print('Tus dos siguientes profesores favoritos son :'+str(TeachersO[2])+ ' and '+str(TeachersO[3]))
print('Tu ultimo profesor favorito es : '+str(TeachersO[-1]))
print('tienes un total de '+str(len(TeachersO))+' Profesor favortio\n')