import math
print('Welcome to the Right Triangle Solver App')

#Obtenemos los catetos y la hipotenusa
leg1 = float(input('What is the first leg of the triangle: '))
leg2 = float(input('What is the second leg of the triangle: '))

# calculamos el area
hypotenuse = round(math.sqrt((math.pow(leg1,2) + math.pow(leg2,2))),3)
area = round((leg1*leg2)/2,3)

print('For a triangle with legs of '+str(leg1)+' and '+str(leg2)+' the hypotenuse is '+str(hypotenuse))
print('For a triangle with legs of '+str(leg1)+' and '+str(leg2)+' the area is '+str(area))
