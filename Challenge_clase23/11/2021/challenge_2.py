print("Welcome to the Miles Per Hour Conversion App\n")

velocidad = float(input(f"What is your speed in miles per hour : "))

print(f" Your speed in mp/h{velocidad}")
velocidad = velocidad * 0.447475
print(f" Your speed in meters per second is {round(velocidad,2)}")
