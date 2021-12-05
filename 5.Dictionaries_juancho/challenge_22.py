
  
print("\tWelcome to the Database Admin Program")

# hemos creado un diccionario con los usuarios en clave 
# y el valor de el diccionario es la contraseña

users = {
    'admin00':'admin1234',
    'mooman':'alskes145',
    'nickyD':'worl1star',
    'george2':'booo3oha',
    'meramo1986':'kehns010101'
}

# queremos saber si el usuario esta en el sistema

user = input("\nEnter your username: ")
if user not in users:
    print("Username not in database, goodbye.")


#Si está continua el programa y si no termina el programa
elif user in users:
    passw = input("Enter your password: ")

    # creamos un operador de comparacion para poder saber si esta en el sistema y si esta dentro utilizandolo
    
    if passw not in users.values():
       print("Password incorrect!")
    elif user == 'admin00':
       print("\nHello ",user,"! You are logged in!")
       print("\nHere is the current user database:")
       
       # creamos un bucle para poder volver a preguntarlo y que no se quede parado el programa
       for clave,valor in users.items():
           print("Username: ",clave,"\t\tPassword: ",valor)
    
    # esto sigue siendo parte de la primra linea if passw not in users.values():
    elif user in users and user != 'admin00':
        print("\nHello ",user,"! You are logged in!")
        c = input("Would you like to change your password: ") 
        
        # en el caso de que quiera cambiar la contraseña 
        if c == 'yes':
            passw2 = input("What would you like your new password to be: ")
            if len(passw2) >= 8:
               print("\n",user," your password is ",passw2)
            elif len(passw2) < 8:
               print(passw2," not the minimum eight characters.")
               print("\n",user," your password is ",passw)
        elif c == 'no':
            print("Goodbye!")
            # por si no es correcto el valor 
        else:
            print("Invalid value")

