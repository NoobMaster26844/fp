Algoritmo Calculadora
	Definir a,b,x Como Real
	Escribir "Escribe dos numeros"
	leer a,b
	x = 0
	Mientras x <> 5 Hacer
		Escribir "Elige una opci�n"
		Escribir "1 = Suma"
		Escribir "2 = Resta"
		Escribir "3 = Multiplicaci�n"
		Escribir "4 = Divisi�n"
		Escribir "5 = Salir"
		Leer x
		
		Segun x
			1:
				Escribir "La suma de ",a," + ",b," = ",a+b
			2:
				Escribir "La resta de ",a," - ",b," = ",a-b
			3:
				Escribir "La multiplicaci�n de ",a," x ",b," = ",a*b
			4:
				Escribir "La divisi�n de ",a," / ",b," = ",a/b
			De otro Modo:
				x = 5
		FinSegun
	FinMientras
	
FinAlgoritmo
