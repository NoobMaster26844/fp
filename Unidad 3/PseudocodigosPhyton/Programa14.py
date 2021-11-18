#Desarrollar un algoritmo para realizar sorteos.

import random
a=int(input("Ingrese el número inicial del sorteo: "))
b=int(input("Ingrese el ultimo numero del sorteo: "))
 
print("el ganador del sorteo es ",random.randint(a,b))