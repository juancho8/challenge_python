print("Welcome to the Temperature Conversion App")
Fahrenheit= float(input("What is the given temperature in degrees Fahrenheit: "))
print(f"{Fahrenheit}")
Celcius = (Fahrenheit-32)*1.8
print(f"Degrees celcius : {round(Celcius,4)}")
kelvin = Fahrenheit +273
print(f"Degrees kelvin : {round(kelvin,4)}")