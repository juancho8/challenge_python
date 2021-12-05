
import random
# libreria random nos sirve para sacar un numero random
dic = {
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']
}
#este diccionario contiene 4 listas con los respecivos sinonimos 
print("\tWelcome to the Thesaurus App!")
print("\nChoose a word from the thesaurus and I will give you a synonym.")
# el usuario debera introducir una palabra 
print("\nHere are the words in the thesaurus:")



# bucle for nos servira para poder ejecutar los sinonimos y 
for i in dic.keys():
    print("\t-",i)
choice = input("\nWhat word would you like a synonym for: ")
x = random.randint(1,5)
if choice in dic:
    print("A synonym for ",choice," is ",dic[choice][x])
#Si esa palabra no se encuentra en el diccionario se imprime un aviso
else:
    print("The word entered does not exist")
c = input("\nWould you like to see the whole thesaurus (yes/no) ").lower()
#Ahora le preguntamos si quiere ver el contenido del diccionario
if c == 'yes':
    for clave in dic:
        print("\n",clave.capitalize()," synonyms are:")
        for i in range(5):
            print("\t-",dic[clave][i])
if c =='no':
    print("I hope you enjoyed the program. Thank you!")