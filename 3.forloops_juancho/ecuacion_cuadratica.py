
import cmath  
# usamos c math ya que con math no soporta este tipo de operaciones complejas.
#Introduccion:
print('Bienvenido a la calculadora de ecuaciones cuadraticas')
print('Una Operacion cuadratica tine forma de : ax^2 + bx + c = 0\nNuestras soluciones pueden ser numeros realmente complejo.\n Un numero complejo tiene 2 partes: a + bj.\nDonde a es la parte real y bj es la parte "imaginaria".')

#Introducimos el input
equations = int(input('Cuantas ecuaciones le gustaria resolver hoy: '))

#resolvemos la ecuacion 
for i in range(1,equations+1):
    print('Resolviendo ecuacion #'+str(i)+'\n---------------------------------------------------------------')
    a = float(input('Por favor introduce el valor de  a (coefficient of x^2): '))
    b = float(input('Por favor introduce el valor de b (coefficient of x): '))
    c = float(input('Por favor introduce el valor de c (coefficient): '))


    d = (b**2) - (4*a*c)  

    #Calculamos la solucion con cmath.sqrt
    x1 = (-b-cmath.sqrt(d))/(2*a)  
    x2 = (-b+cmath.sqrt(d))/(2*a) 


    print('\nLa solucion de '+str(a)+'x^2 + '+str(b)+'x + '+str(c)+' = 0 es : ')
    print('x1 = '+str(x1)+'\nx2 = '+str(x2))
    
