#Pedir el nombre de 5 peliculas y al seleccionar una te de el nombre

peliculas = ["Harry Potter y la piedra filosofal", "Harry Potter y la camara secreta", "Harry Potter y el prisionero de askaban", "Harry Potter y el caliz de fuego", "Harry Potter y la orden del fenix"]
print ("Peliculas: "
"(0 = Harry Potter y la piedra filosofal) "
"(1 = Harry Potter y la camara secreta) "
"(2 = Harry Potter y el prisionero de askaban) "
"(3 = Harry Potter y el caliz de fuego) "
"(4 = Harry Potter y la orden del fenix) ")

x = int (input("Ingresar el numero de la pelicula: "))
p = peliculas [x]

print (p)
print ("Finalizado")