promedio = 7
nombre = input ("Ingresar el nombre del alumno")
calif = int(input("Ingresar la calificacion: "))

if calif > promedio:
    print(nombre)
    print("Aprobo")
elif calif < promedio:
    print(nombre)
    print("Reprobo")
else:
    print("Calificacion no admitida")

print("Fin")