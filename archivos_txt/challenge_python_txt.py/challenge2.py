from os.path import exists

# importamos la bibloteca para comprobar que nuestro dato existe
def leer_tabla_multiplicar():  
  n = int(input('por favor Introduce un número entero entre 1 y 10: '))
  file_name = 'tabla' + str(n) + '.txt'
  try: 
      f = open(file_name, 'r')
  except FileNotFoundError:
      print('ERROR ! No existe el fichero con la tabla del', n)
  else:
      print(f.read())
  f.close()



file_exists = exists('./tabla-5.txt')

print(file_exists)