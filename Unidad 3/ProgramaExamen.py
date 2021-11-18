#Desarrollar un programa que guarde a todos los integrantes del grupo como objetos con los siguientes atributos 
#(Edad, Calificación de las diferentes materias, promedio, calificación de la prepa y lugar de residencia)
#Imprimir los siguientes reportes:
#(5 alumnos con mayor de edad, Promedio de todos en la prepa, Alumnos que viven cerca y mas lejos, materia con mejor rendimiento)

#Clase
class alumno():
	def __init__(self,edad,nombre,calculo,FDP,FDI,introtics,matematicas,ingles,etica,califprepa,lugarresidencia,distanciatec):
		self.nombre = nombre
		self.edad = edad
		self.calculo = calculo
		self.FDP = FDP
		self.FDI = FDI
		self.matematicas = matematicas
		self.ingles = ingles
		self.etica = etica
		self.califprepa = califprepa
		self.lugarresidencia = lugarresidencia
		self.distanciatec = distanciatec

#Objetos
reyna = alumno(18,"Reyna",9,8,10,10,9,6,7,9,"Emiliano Zapata",13)
mirozlava = alumno(18,"Sharlene",9,7,8,7,8,9,7,8,"Cosio",27)
melany = alumno(18,"Melany",6,9,7,8,9,7,8,9,"Pabellón,",5)
diego = alumno(19,"Diego",7,9,8,7,9,10,8,9,"Rincón",13)
britzy = alumno(18,"Britzy",8,7,9,8,9,7,8,9,"Rincón",13)
fernando = alumno(17,"Fernando",7,8,7,9,8,7,8,9,"Pabellón",5)
alejandra = alumno(18,"Alejandra",10,10,10,9,7,8,8,9,"Jesús Maria",27)
alejandro = alumno(19,"Alejandro",8,9,7,9,7,8,6,8,"Ejido Fresnillo",17)
donaldo = alumno(18,"Donaldo",10,10,10,10,9,9,8,9,"San José de Gracia",18)
austin = alumno(18,"Austin",10,10,10,10,10,9,9,9,"Pabellón",5)
paola = alumno(18,"Paola",10,10,9,8,9,9,7,8,"Carboneras",8)
isaac = alumno(19,"Isaac",10,9,10,9,10,10,10,9,"rincon",13)
areli = alumno(19,"Areli",10,9,10,9,10,9,10,8,"rincon",13)
alain = alumno(18,"Alain",10,9,10,9,10,9,10,8,"asientos",11)
alexis = alumno(19,"Alexis",10,9,10,8,7,8,7,8,"rincon",13)

#Alumnos con mayor edad
print("Los alumnos mayores son: ", diego.nombre,",",alejandro.nombre,",",isaac.nombre,",",areli.nombre,"y",alexis.nombre )

#alumnos con su promedio
print ("Promedio de los alumnos:\n", reyna.nombre,"con promedio de",reyna.califprepa,",\n",mirozlava.nombre,"con promedio de",mirozlava.califprepa)
print(melany.nombre,"con promedio de",melany.califprepa,",\n",diego.nombre,"con promedio de",diego.califprepa,",\n",britzy.nombre,"con promedio de",britzy.califprepa)
print(fernando.nombre,"con promedio de",fernando.califprepa,",\n",alejandra.nombre,"con promedio de",alejandra.califprepa,",\n",alejandro.nombre,"con promedio de",alejandro.califprepa)
print(donaldo.nombre,"con promedio de",donaldo.califprepa,",\n",austin.nombre,"con promedio de",austin.califprepa,",\n",paola.nombre,"con promedio de",paola.califprepa)
print(isaac.nombre,"con promedio de",isaac.califprepa,",\n",areli.nombre,"con promedio de",areli.califprepa,",\n",alain.nombre,"con promedio de",alain.califprepa,",\n",alexis.nombre,"con promedio de",alexis.califprepa)

#alumnos que viven mas cerca y mas lejos
print("Los alumnos mas lejanos al TEC son:\n",mirozlava.nombre,"es de ",mirozlava.lugarresidencia, "con una distancia de", mirozlava.distanciatec, "y\n", alejandra.nombre, "es de", alejandra.lugarresidencia, "con una distancia de",alejandra.distanciatec )
print("Los alumnos mas cercanos al TEC son:\n",melany.nombre,"es de ",melany.lugarresidencia, "con una distancia de", melany.distanciatec, "y\n", donaldo.nombre, "es de", donaldo.lugarresidencia, "con una distancia de",donaldo.distanciatec )

#alumnos y su mejor calificacion de materia
print ("los alumnos y sus mejoras se presentaran a continuación\n", reyna.nombre,"con la meteria de fundamentos de la programacion",",\n",mirozlava.nombre,"con la meteria de fundamentos de la investigación")
print(melany.nombre,"con la materia de fundamentos de la investigacion",",\n",diego.nombre,"con la materia de fundamentos de mates discretas",",\n",britzy.nombre,"con la materia de calculo diferencial")
print(fernando.nombre,"con la materia de matematicas discretas",",\n",alejandra.nombre,"con la materia de introduccion a las tics",",\n",alejandro.nombre,"con la materia de calculo diferencial")
print(donaldo.nombre,"con la materia de calculo diferencial",",\n",austin.nombre,"con la materia de ingles ",",\n",paola.nombre,"con la materia de calculo diferencial ")
print(isaac.nombre,"con la materia de calculo diferencial",",\n",areli.nombre,"con la materia de fundamentos de la investigacion",",\n",alain.nombre,"con la materia de ingles",",\n",alexis.nombre,"con la materia de calculo diferencial ")