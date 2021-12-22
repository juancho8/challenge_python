print('Welcome to the Multiplication/Exponent Table App')

# optenemos los outputs de los usuarios.
name = str(input('What is your name: '))
number = float(input('What number would you like to work with: '))

print('\nMultiplication Table for '+str(number)+'\n')
for i in range(1,9):
    print(str(i)+' * '+str(number)+' = '+str(i*number))


print('\nExponent Table for '+str(number)+'\n')
for i in range(1,10):
    print(str(number)+' ** '+str(i)+' = '+str(number**i))

frase = 'math is cool!' 
print(+str(name.capitalize())+' '+str(frase.capitalize()))
print(+str(name.lower())+' '+str(frase.lower()))
print(+str(name.title())+' '+str(frase.title()))
print(+str(name.upper())+' '+str(frase.upper()))