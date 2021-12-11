Algoritmo Calculadora
	Definir a,b,x Como Real
	Escribir "Escribe dos numeros"
	leer a,b
	x = 0
	Mientras x <> 5 Hacer
		Escribir "Elige una opción"
		Escribir "1 = Suma"
		Escribir "2 = Resta"
		Escribir "3 = Multiplicación"
		Escribir "4 = División"
		Escribir "5 = Salir"
		Leer x
		
		Segun x
			1:
				Escribir "La suma de ",a," + ",b," = ",a+b
			2:
				Escribir "La resta de ",a," - ",b," = ",a-b
			3:
				Escribir "La multiplicación de ",a," x ",b," = ",a*b
			4:
				Escribir "La división de ",a," / ",b," = ",a/b
			De otro Modo:
				x = 5
		FinSegun
	FinMientras
	
FinAlgoritmo
