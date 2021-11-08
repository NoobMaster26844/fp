promedio = 7
running = True

while running:
    nombre = input ("Ingresar el nombre del alumno: ")
    calif = int(input("Ingresar la calificacion: "))

    if calif > promedio:
        print(nombre)
        print("Aprobo")
    elif calif < numero:
        print(nombre)
        print("Reprobo")
    else:
        print(nombre, "Reprobo")
else:
    print("El bucle termino")

print("FIN")