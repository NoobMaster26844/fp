#Programa sorteo del número 1 al 10

w =int(input("Elige un numero del 1 al 10: "))
import random
c = random.randint(1,10)

if w == c:
	print("El boleto ganador es: ",w)
else:
	print(w," Sigue participando.")

print("Fin")