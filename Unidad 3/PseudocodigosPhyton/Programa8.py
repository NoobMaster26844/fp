#Pedir tres numeros e imprimir el numero mayor

numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))
numero3 = int(input("Ingresa otro numero: "))

if (numero1) > (numero2):
	if (numero1) > (numero3):
		print ("El numero mayor es: ",numero1)
elif (numero3) > (numero1):
		print ("El numero mayor es: ",numero3)
else: 
	if (numero2) > (numero3):
		print ("El numero mayor es: ",numero2)

print ("Finalizado")