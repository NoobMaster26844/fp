#Programa que te estime el tiempo de llegada a un destino con base en la velocidad y distancia

distancia =int(input("Ingresa la distancia en kilometros: "))
velocidad =int(input("Ingresa la velocidad en kilometros por hora: "))

tiempo = distancia / velocidad
print("El tiempo por ",distancia," kilometros recorridos es: ",tiempo, " horas")
print("Fin")