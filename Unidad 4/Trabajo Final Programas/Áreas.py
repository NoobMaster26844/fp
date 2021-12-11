#Programa que saque el área de un círculo, un cuadrado, rectángulo y triángulo

print("Operaciones: ")
print("1 = área del cuadrado")
print("2 = área del rectangulo")
print("3 = área del triangulo")
print("4 = área del circulo")
x =int(input("¿Qué área quieres sacar?:"))

if x == 1:
	a =int(input("Ingresa uno de los lados del cuadrado: "))
	print("El área del cuadrado es:",a*a)
elif x == 2:
	a =int(input("Ingresa la base: "))
	b =int(input("Ingresa la altura: "))
	print("El área del rectangulo es:",a*b)
elif x == 3:
	a =int(input("Ingresa la base: "))
	b =int(input("Ingresa la altura: "))
	print("El área del triangulo es:",(a*b)/2)
elif x == 4:
	a =int(input("Ingresa el radio: "))
	print("El área del circulo es:",3.1416 * a * a)
print("FIN")
