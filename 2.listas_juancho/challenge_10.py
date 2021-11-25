
print("Welcome to the Favorite Teachers Program ")
first = input("Who is your first favorite teacher: \n ")
print(f"{first}")
second = input("Who is your second favorite teacher: \n ")
print(f"{second}")
third = input("Who is your third favorite teacher: \n ")
print(f"{third}")
fourth = input("Who is your fourth favorite teacher: \n ")
print(f"{fourth}")
lista_teachers=[first,second,third,fourth]
print(f"{lista_teachers}")
print(f"{sorted(lista_teachers)}")
print(f"{sorted(lista_teachers ,reverse=True)}")

print(f"Your top two teachers are {lista_teachers[0,1]}")
print(f"Your next two top teachers are {lista_teachers[2,3]}")
print(f"Your last favourite teacher is {lista_teachers[3]}")
print(f"{len(lista_teachers)}")

print(f"OOps {lista_teachers[0] } is no longer your favourit teacher . Who is your new favourite Teacher :")
lista_teachers.insert(input(""))
lista_teachers[1]= 

x[1] = "r"
x[2:] = ["s", "t"]
x = ["a", "b", "c", "d"]
