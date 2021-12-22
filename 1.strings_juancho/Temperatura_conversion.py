print('Welcome to the Temperature Conversion App')

# Obtenemos el valor en fahrenheit 
fahrenheit = float(input('What is the given temperature in degrees Fahrenheit: '))
celsius = round( (fahrenheit - 32) * 5/9,4)
kelvin = round(((fahrenheit - 32) * 5/9 + 273.15),4)
# calculos y output
print('Degrees Fahrenheit: '+str(fahrenheit)+'\nDegrees Celsius: '+str(celsius)+'\nDegrees Kelvin: '+str(kelvin))