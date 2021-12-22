print('Bienvenido a la calculadora de HEXADECIMAL_A_BINARIO')

#Get the input
list = int(input('Por favor introduce los valores en HEXADECIMAL Y BINARIO '))

#Get two nums from user
print('A continuacionn mostraremos una porcion de la lista.')
startNum = int(input('En que numero decimal le gustaria comenzar : '))
stopNum = int(input('En que numero decimal le gustaria finalizar : '))

#Print decimal values between 'startNum' and 'stopNum'
print('Los decimales van desde  '+str(startNum)+' hasta '+str(stopNum))
for i in range(startNum,stopNum):
    print(i)

#Print binary values between 'startNum' and 'stopNum'
print('Binary values from '+str(startNum)+' to '+str(stopNum))
for i in range(startNum,stopNum):
    print(bin(i))

#Print hexadecimal values between 'startNum' and 'stopNum'
print('Los hexadecimales van desde'+str(startNum)+' hasta '+str(stopNum))
for i in range(startNum,stopNum):
    print(hex(i))

#Print values from 1 to 'list' Decimal --- Binary ---- Hexadecimal
input('Presiona enter para mostral los valores  '+str(list)+'.')
print('Decimal----Binario----Hexadecimal \n----------------------------------------------------------')
for i in range(1,list+1):
    print(str(i)+'----'+str(bin(i))+'----'+str(hex(i)))