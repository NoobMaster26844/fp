#Programa que ingreses el nombre completo de dos personas y te cuente el número de letras de cada nombre. Después que imprima cual es mayor.

n1 = input("Ingresa el primer nombre completo: ")
n2 = input("Ingresa el segundo nombre completo: ")
x = len (n1)
z = len (n2)

if len(n1) > len(n2):
	print("El nombre mas largo es: ",n1)
	print("La cantidad de caracteres es: ",x)
else:
	print("El nombre mas largo es: ",n2)
	print("La cantidad de caracteres es: ",z)
