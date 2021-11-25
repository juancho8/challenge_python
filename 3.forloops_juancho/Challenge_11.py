print("Welcome to the Binary/Hexadecimal Converter App")
print("Compute binary and hexadecimal values up to de following decimal number: ")
numero = int(input())
print(f"{numero}")
print("Generating lists...Complete!")
print("Using slices, we will now show a portion of each list.")

print("What decimal number would you like to start at: ")
decimal_start = int(input())
print(f"{decimal_start}")
print("at decimal number would you like to stop at:" )
decimal_stop = int(input())
print(f"{decimal_stop}")

lista_numeros = range(1,numero)


print(lista_numeros[decimal_start:decimal_stop])

bin_lista = []
hex_lista = []

for numero in lista_numeros:
    bin_lista.append(bin(numero))
    hex_lista.append(hex(numero))


print(f"\tDecimal values from {decimal_start} to {decimal_stop} ")

for i in range(decimal_start-1,decimal_stop):
    print(f"\t{lista_numeros[i]}")

for i in range(decimal_start-1,decimal_stop):
    print(f"\t{bin_lista[i]}")

for i in range(decimal_start-1,decimal_stop):
    print(f"\t{hex_lista[i]}")12
    

print(f"Press enter to see al values from 1 to {numero}\n)

espacio  = input("")
if espacio = "\n"
    print("")