Algoritmo PalabrasConMasLetras
	ESCRIBIR 'Ingresa la primera palabra' 
	LEER Palabra1
	ESCRIBIR 'Ingresa la segunda palabra'
	LEER Palabra2
	a= longitud (palabra1);
	c= longitud (palabra2);
	Si a>c ENTONCES 
		ESCRIBIR 'La palabra ' , palabra1 ' es mayor';
		SiNo
			Si c>a Entonces 
				Escribir 'La palabra ' , palabra2 ' es mayor';
			FinSi
	FinSi
	
FinAlgoritmo
