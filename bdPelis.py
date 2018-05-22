#Luis Esturban
from neo4jrestclient.client import GraphDatabase
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="123")
 
# Create some nodes with labels
generos = db.labels.create("Generos")
peliculas = db.labels.create("Peliculas")
actores = db.labels.create("Actores")


def menu():
    print ("***********************************************")
    print ("Sistema de recomendacion medica")
    print ("1. Ingresar Genero")
    print ("2. Ingresar Pelicula")
    print ("3. Ingresar Actor")
    print ("4. Relacion entre Genero y Pelicula")
    print ("5. Relacion entre Pelicula y Actor")
    print ("6. Consultar Generos")
    print ("7. Consultar Actores")
    print ("8. Consultar Peliculas por Genero")
    print ("9. Consultar Peliculas por Actor")
    print ("10. Salir")
    print ("***********************************************")
    print (" ")
#Este bloque es para prueba
#Hacer lo mismo solo que automatico
#----------------------------------------------------------------    
#Funcion para ingresar genero
def ingresarGen():
    gen = input("Ingrese el nombre del Genero: ")
    genero = db.nodes.create(nombreGen=gen)
    generos.add(genero)
#Funcion para agregar pelicula
def ingresarPel():
    pel = input("Ingrese el nombre del Genero: ")
    pelicula = db.nodes.create(nombrePel=pel)
    peliculas.add(pelicula)
#Funcion para agregar Actor
def ingresarAct():
    act = input("Ingrese el nombre del Genero: ")
    actor = db.nodes.create(nombreAct=act)
    actores.add(actor)
#Gustavo este es el que hay que cambiar para que sea alreves
#Funcion para relacionar peliculas con generos
def relacionPel_Gen():
     gen1 = input("Ingrese el genero: ")
     pel1 = input("Ingrese la pelicula: ")
     try: 
         (generos.get(nombreGen=gen)[0]).relationships.create("pertenece", peliculas.get(nombrePel=pell)[0])
        
     except:
         print("No existe algun paciente de los dos o esta mal escrito")
         print(" ")
         print(" ")
#Funcion para relacionar actores con pelicula
def relacionAct_Pel():
     act1 = input("Ingrese el actor: ")
     pel2 = input("Ingrese la pelicula: ")
     try: 
         (actores.get(nombreAct=act1)[0]).relationships.create("actua", peliculas.get(nombrePel=pel2)[0]) 
     except:
         print("No existe algun paciente de los dos o esta mal escrito")
         print(" ")
         print(" ")
#----------------------------------------------------------------------------------------------------------------------------------------

#Funcion para consultar genero
def consultarGen():
    try:
        query = "MATCH (n:Generos) RETURN n"
        results = db.query(query, data_contents=True)
        a = results.rows
        for list in a:
            for x in list:
                print (x)
    except:
         print("No hay ningun doctor con esa especialidad o esta mal escroto")
         print(" ")
         print(" ")
#Funcion para consultar actor
def consultarAct():
    conAct = input("Ingrese la especialidad: ")
    try:
        query = "MATCH (n:Actores {nombreAct:'"+conAct+"'}) RETURN n"
        results = db.query(query, data_contents=True)
        a = results.rows
        for list in a:
            for x in list:
                print (x)
    except:
         print("No hay ningun doctor con esa especialidad o esta mal escroto")
         print(" ")
         print(" ")
#Funcion para consultar pelicula por medio de su genero
def consultarPel_Gen():
    gen3 = input("Ingrese el genero que desea buscar: ")
    try:
         query = "MATCH (p:Peliculas{nombrePel:'"+gen3+"'})-[:pertenece]->(d:Generos) return d"
         results = db.query(query, data_contents=True)
         a = results.rows
         b = []
         for x in a:
             if x not in b:
                 b.append(x)
                 print (x)
         print(" ")
         print(" ")
    except:
         print("No tiene algun amigo que le recomiende esta especialidad ")
         print("O lo escribio mal ")
         print(" ")
#Funcion para consultar pelicula por medio de su actor    
def consultarPel_Act():
    gen3 = input("Ingrese el genero que desea buscar: ")
    try:
         query = "MATCH (p:Actores{nombreAct:'"+gen3+"'})-[:actua*1..2]->(d:Peliculas{nombrePel:'"+pel3+"'}) return d"
         results = db.query(query, data_contents=True)
         a = results.rows
         b = []
         for x in a:
             if x not in b:
                 b.append(x)
                 print (x)
         print(" ")
         print(" ")
    except:
         print("No tiene algun amigo que le recomiende esta especialidad ")
         print("O lo escribio mal ")
         print(" ")

#Ciclo principal para menu  
opcion = 0
while (opcion != 8):
	# Mostramos el menu
	menu()
 
	# solicitamos una opción al usuario
	opcion = int(input("Ingrese el numero que desea realizar: "))
 
	if opcion==1:		
		ingresarGen()
	elif opcion==2:
		ingresarPel()
	elif opcion==3:
		ingresarAct()
	elif opcion==4:
		relacionPel_Gen()
	elif opcion==5:
		relacionAct_Pel()
	elif opcion==6:
		consultarGen()
	elif opcion==7:
		consultarAct()
	elif opcion==8:
		consultarPel_Gen()
	elif opcion==9:
		consultarPel_Act()
	elif opcion==10:
		sys.exit()

                
