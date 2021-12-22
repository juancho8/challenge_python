print('Welcome to the Grade Sorter App')


grades = []
for i in range(4):
    grades.append(int(input('What is your '+str(i+1)+'° note (0-100): ')))
# recibimos las notas de los usuarios
print('Your grades are: '+str(grades))

# usamos la funcion sort con nuestra lista
grades.sort(reverse=True)
print('Your grades from highest to lowest are: '+str(grades)+
'\nThe lowest two grades will now be dropped.'
'\nRemoved grade: '+str(grades[2])+
'\nRemoved grade: '+str(grades[3]))



del grades[2:4]# quitamos las ultimas 2 notas
print('Your remaining grades are: '+str(grades))
print('Nice work! Your highest grade is: '+str(grades[0]))