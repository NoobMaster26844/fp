#Programa que pida nombre y edad e imprima el mas grande

Nombre1 = input("Ingresar Nombre: ")
Edad1 = int(input("Ingrasar Edad: "))
Nombre2 = input("Ingresar Nombre: ")
Edad2 = int(input("Ingresar Edad: "))

if Edad1 > Edad2:
	print(Nombre1, Edad1)
elif Edad1 < Edad2: 
	print(Nombre2, Edad2)
else:
	print("Datos no validos")

print("FIN")