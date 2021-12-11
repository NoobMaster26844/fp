Algoritmo Áreas
	Definir n Como Entero
	Definir a,b Como Real
	n = 0
	Mientras n <> 5 Hacer
		Escribir "¿Qué área quieres sacar?:"
		Escribir "1 = área del cuadrado"
		Escribir "2 = área del rectangulo"
		Escribir "3 = área del triangulo"
		Escribir "4 = área del circulo"
		Escribir "5 = Salir"
		Leer n
		si n == 1 Entonces
			Escribir "Ingresa uno de los lados del cuadrado"
			Leer a
			Escribir "El área del cuadrado es: ",a*a
		SiNo
			si n == 2 Entonces
				Escribir "Ingresa la base"
				Leer a
				Escribir "Ingresa la altura"
				Leer b
				Escribir "El área del rectangulo es: ",a*b
			SiNo
				Si n ==3 Entonces
					Escribir "Ingresa la base"
					Leer a
					Escribir "Ingresa la altura"
					Leer b
					Escribir "El área del triangulo es: ",(a*b)/2
				SiNo
					Si n == 4 Entonces
						Escribir "Ingresa el radio"
						Leer a
						Escribir "El área del circulo es: ",3.1416 * a * a
					FinSi
				FinSi
			FinSi
		FinSi
	FinMientras
	
FinAlgoritmo
