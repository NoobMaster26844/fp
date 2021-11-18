#Pedir 5 calificaciones y obtener promedio

nombre = input("Ingresar nombre: ")
x = ("Ingresar calificaciones: ")
dibujo = int(input("Dibujo:"))
FDI = int(input("Fundamentos de investigacion: "))
ingles = int(input("Ingles:"))
programacion = int(input("Programacion:"))
etica = int(input("Ética"))

calif = (dibujo + FDI + ingles + programacion + etica)
promedio = calif / 5

print (promedio)
print ("Finalizado")