print('Welcome to the Letter Counter App')

# obtenemos el nombre del usuario
name = str(input('What is your name: '))
print('Hello '+str(name)+'!')

print('I will count the number of times that a specific letter occurs in a message.')
message = str(input('Please enter a message: '))

# metemos la letra y contamos las veces que aparece
letter = str(input('Which letter would you like to count the occurrences of: ')).lower()
number = message.lower().count(letter)
print(str(name)+', your message has '+str(number)+'\'s in it.')