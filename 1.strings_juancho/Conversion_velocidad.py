print('Welcome to the Miles Per Hour Conversion App')

#Obtener la velocidad en millas por hora
miles = float(input('What is your speed in miles per hour: '))

# cambiamos de millas por hora a metros por segundo
conversion = round(miles / 2.237,2)
print('Your speed in meters per second is: '+str(conversion))