print("Javier Ignacio Mauro Corrales")
print("")
edad = int(input("Ingrese su edad actual:  "))

diasvividos = edad * 365

with open("dias.txt", "w") as f:

	print(f"Has vivido un estimado de", diasvividos, "dias")
