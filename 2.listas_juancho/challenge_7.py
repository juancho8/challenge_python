print("the variable num_strings is a <class'list>\n")
hard_code=['15','100','55','42']
print(f"It contains the elements: [{hard_code}]")
print("\nThe element 15 is a <class 'int'>")
print("\nthe variable num_ints is a <class'list'>")

# creamos una lista llamada hard_code la cual usaremos para meter nuestros valores en forma de string 

hard_code1=[15,100,55,42]
print(f"\nIt contains the elements: [{hard_code}]")
print("\nThe element 15 is a <class 'int'>")
print("\nThe variable num_floats is a <class'list>")


hard_code2=[[1,2,3],[1,2,3],[1,2,3]]
print(f"\nIt contains the elements: [{hard_code}]")
print("\nThe element 15 is a <class 'list'>")
print("\nThe varable num_ints is a <class list'")

#funcion sorted sirve para ordenar numeros y palabras
hard_code=sorted(hard_code)
num_ints=hard_code

hard_code2=sorted(hard_code2)
num_ints=hard_code

print(f' \nNow sorting num_strings and num_ints...')
print(f' \nSorted num_strings:{hard_code}')
print(f' \nSorted num_ints: {hard_code2}')
#se puede hacer variable.sort pero no funciona eta vez
#vamos a usar sorted
#puse salto de linea en todos porque asi se puede leer
