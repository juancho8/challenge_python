notas = []
print("Welcome to the Grade Sorter App")
grade1 = int(input("\nWhat is your first grade(0-100): "))
notas.insert(1,grade1)
grade2 = int(input("\nWhat is your first grade(0-100): "))
notas.insert(2,grade2)
grade3 = int(input("\nWhat is your first grade(0-100): "))
notas.insert(3,grade3)
grade4 = int(input("\nWhat is your first grade(0-100): "))
notas.insert(4,grade4)
# creamos 4 variables una para cada nota 
# insertamos con la funcion insert la cual se usa para listas

print(f"\nYour grades are :[ {grade1},{grade2},{grade3},{grade4}]")

notas=sorted(notas, reversed=True)
#se puede hacer variable.sort pero no funciona eta vez
#vamos a usar sorted


print(f"\nYour grades are :[{notas}]")
print(f"\nThe lowest two grades will be droped")
print(f"\nRemoved grade: {grade3} \nRemoved grade: {grade4} ")
notas.pop(2)
# .pop nos permite retirar un valor de nuestra lista
notas.pop(2)
print(f"\nYour remaining grades are : [{grade1},{grade2}]")
print(f"\nNice work! Your hights grade is {grade1}")