#Calculadora que sume, reste, multiplique y divida.

print("Operaciones: ")
print("1 = Suma")
print("2 = Resta")
print("3 = Multiplicación")
print("4 = División")
x =int(input("¿Qué deseas hacer?:"))

if x == 1:
	a =int(input("Ingresa un numero: "))
	b =int(input("Ingresa otro numero: "))
	print("La suma de ",a," + ",b," = ",a+b)
elif x == 2:
	a =int(input("Ingresa un numero: "))
	b =int(input("Ingresa otro numero: "))
	print("La resta de ",a," - ",b," = ",a-b)
elif x == 3:
	a =int(input("Ingresa un numero: "))
	b =int(input("Ingresa otro numero: "))
	print("La multiplicación de ",a," x ",b," = ",a*b)
elif x == 4:
	a =int(input("Ingresa un numero: "))
	b =int(input("Ingresa otro numero: "))
	print("La división de ",a," / ",b," = ",a/b)
print("FIN")