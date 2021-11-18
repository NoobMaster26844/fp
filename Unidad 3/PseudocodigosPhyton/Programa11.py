#Hacer un programa que pida las calificaciones y te muestre si esta aprobado o reprobado

a=int(input("Ingrese la cantidad de calificaciones: "))
b=1
d=0

while a>=b:
		b=b+1
		c=int(input("Ingrese su calificación: "))
		d=c+d
		e=d/a
		if e>=7:
				print ("¡Felicidades Aprobaste!")