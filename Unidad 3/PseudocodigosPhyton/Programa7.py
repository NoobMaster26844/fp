#Imprimir el numero mayor

numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))

if numero1 < numero2:
	print("El numero mayor es ",numero2)
elif numero1 > numero2:
	print("El numero mayor es ",numero1)
else:
	print("error")

print("Finalizado")