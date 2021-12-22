print('BIENVENIDO A LA CALCULADORA FIBONNACI')

#CALCULANDO FIBONACCI CON LOS VALORES DE LA LISTA 
num = int(input('Cuantos numeros de la serie fibonnaci quieres que imprima: '))
Fibonnaci = []
actual = 0
for i in range(num):
    if i==0:
        Fibonnaci.append(i+1)
    elif  i==1:
        Fibonnaci.append(i)
    else:
        Fibonnaci.append(Fibonnaci[i-1]+Fibonnaci[i-2])
print(*Fibonnaci)  

#CALCULANDO EL " GOLDEN RATIO"
print('Los numeros correspondientes al golden ratio son : ')
gold = []
for i in range(num):
    if i==0:
        gold.append(float(i+1.0))
    elif  i==1:
        gold.append(float(i+1.0))
    else:
        ratio = (gold[i-2]%gold[i-1])+(gold[i-2]/gold[i-1])
        gold.append(ratio)     
print(*gold)