Algoritmo Nombres_y_Numero_de_Letras
	Escribir "Ingresa el primer nombre completo: "
	Leer N1
	Escribir "Ingresa el segundo nombre completo: "
	Leer N2
	x= Longitud(N1)
	z = Longitud(N2)
	
	Si Longitud(N1) > Longitud(N2) Entonces
		Imprimir "Nombre más largo: ",(N1) 
		Imprimir "La cantidad de caracteres es: ",x
	SiNo
		Imprimir "Nombre más largo: ",(N2) 
		Imprimir "La cantidad de caracteres es: ",z
	FinSi
	
FinAlgoritmo
