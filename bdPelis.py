#Luis Esturban
#Gustavo De Leon 
from neo4jrestclient.client import GraphDatabase
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="159753")
 
# Create some nodes with labels
generos = db.labels.create("Generos")
peliculas = db.labels.create("Peliculas")
actores = db.labels.create("Actores")
try:
    query = "MATCH (n:Generos) RETURN n"
    results = db.query(query, data_contents=True)
    a = results.rows
    for list in a:
        for x in list:
            print (" ")
except:
    #Generos programados
    accion = db.nodes.create(nombreGen="Accion")
    generos.add(accion)
    terror = db.nodes.create(nombreGen="Terror")
    generos.add(terror)
    drama = db.nodes.create(nombreGen="Drama")
    generos.add(drama)
    comedia = db.nodes.create(nombreGen="Comedia")
    generos.add(comedia)
    ficcion = db.nodes.create(nombreGen="Ficcion")
    generos.add(ficcion)
    romance = db.nodes.create(nombreGen="Romance")
    generos.add(romance)
    musical = db.nodes.create(nombreGen="Musical")
    generos.add(musical)
    #Peliculas programadas
    deadpool_2 = db.nodes.create(nombrePel="Deadpool 2")
    peliculas.add(deadpool_2)
    deadpool = db.nodes.create(nombrePel="Deadpool")
    peliculas.add(deadpool)
    avengers = db.nodes.create(nombrePel="Avengers 1")
    peliculas.add(avengers)
    avengers2 = db.nodes.create(nombrePel="Avengers 2")
    peliculas.add(avengers2)
    avengers3 = db.nodes.create(nombrePel="Avengers 3")
    peliculas.add(avengers3)
    starw1 = db.nodes.create(nombrePel="Star Wars 1")
    peliculas.add(starw1)
    starw2 = db.nodes.create(nombrePel="Star Wars 2")
    peliculas.add(starw2)
    starw3 = db.nodes.create(nombrePel="Star Wars 3")
    peliculas.add(starw3)
    starw4 = db.nodes.create(nombrePel="Star Wars 4")
    peliculas.add(starw4)
    starw5 = db.nodes.create(nombrePel="Star Wars 5")
    peliculas.add(starw5)
    starw6 = db.nodes.create(nombrePel="Star Wars 6")
    peliculas.add(starw6)
    starw7 = db.nodes.create(nombrePel="Star Wars 7")
    peliculas.add(starw7)
    starw8 = db.nodes.create(nombrePel="Star Wars 8")
    peliculas.add(starw8)
    saw1 = db.nodes.create(nombrePel="Saw 1")
    peliculas.add(saw1)
    saw2 = db.nodes.create(nombrePel="Saw 2")
    peliculas.add(saw2)
    saw3 = db.nodes.create(nombrePel="Saw 3")
    peliculas.add(saw3)
    saw4 = db.nodes.create(nombrePel="Saw 4")
    peliculas.add(saw4)
    saw5 = db.nodes.create(nombrePel="Saw 5")
    peliculas.add(saw5)
    saw6 = db.nodes.create(nombrePel="Saw 6")
    peliculas.add(saw6)
    saw7 = db.nodes.create(nombrePel="Saw 7")
    peliculas.add(saw7)
    it = db.nodes.create(nombrePel="It")
    peliculas.add(it)
    titanic = db.nodes.create(nombrePel="Titanic")
    peliculas.add(titanic)
    padrino1 = db.nodes.create(nombrePel="El Padrino 1")
    peliculas.add(padrino1)
    padrino2 = db.nodes.create(nombrePel="El Padrino 2")
    peliculas.add(padrino2)
    padrino3 = db.nodes.create(nombrePel="El Padrino 3")
    peliculas.add(padrino3)
    forrest = db.nodes.create(nombrePel="Forrest Gump")
    peliculas.add(forrest)
    pianista = db.nodes.create(nombrePel="El Pianista")
    peliculas.add(pianista)
    hachiko = db.nodes.create(nombrePel="Hachiko")
    peliculas.add(hachiko)
    gladiador = db.nodes.create(nombrePel="Gladiador")
    peliculas.add(gladiador)
    hangover1 = db.nodes.create(nombrePel="Hangover 1")
    peliculas.add(hangover1)
    hangover2 = db.nodes.create(nombrePel="Hangover 2")
    peliculas.add(hangover2)
    hangover3 = db.nodes.create(nombrePel="Hangover 3")
    peliculas.add(hangover3)
    scary1 = db.nodes.create(nombrePel="Scary Movie 1")
    peliculas.add(scary1)
    scary2 = db.nodes.create(nombrePel="Scary Movie 2")
    peliculas.add(scary2)
    scary3 = db.nodes.create(nombrePel="Scary Movie 3")
    peliculas.add(scary3)
    scary4 = db.nodes.create(nombrePel="Scary Movie 4")
    peliculas.add(scary4)
    scary5 = db.nodes.create(nombrePel="Scary Movie 5")
    peliculas.add(scary5)
    superbad = db.nodes.create(nombrePel="Superbad")
    peliculas.add(superbad)
    click = db.nodes.create(nombrePel="Click")
    peliculas.add(click)
    ninos1 = db.nodes.create(nombrePel="Son Como Ninos 1")
    peliculas.add(ninos1)
    ninos2 = db.nodes.create(nombrePel="Son Como Ninos 2")
    peliculas.add(ninos2)
    zohan = db.nodes.create(nombrePel="Zohan")
    peliculas.add(zohan)
    notebook = db.nodes.create(nombrePel="The Notebook")
    peliculas.add(notebook)
    lalala = db.nodes.create(nombrePel="La la land")
    peliculas.add(lalala)
    dear = db.nodes.create(nombrePel="Dear John")
    peliculas.add(dear)
    primera = db.nodes.create(nombrePel="Como la primera vez")
    peliculas.add(primera)
    crepusculo = db.nodes.create(nombrePel="Crepusculo")
    peliculas.add(crepusculo)
    grease = db.nodes.create(nombrePel="Grease")
    peliculas.add(grease)
    high1 = db.nodes.create(nombrePel="High School Musical")
    peliculas.add(high1)
    high2 = db.nodes.create(nombrePel="High School Musical 2")
    peliculas.add(high2)
    high3 = db.nodes.create(nombrePel="High School Musical 3")
    peliculas.add(high3)
    
    #Actores programados
    Ryan_Reynolds = db.nodes.create(nombreAct="Ryan Reynolds")
    actores.add(Ryan_Reynolds)
    Chris_Evans = db.nodes.create(nombreAct="Chris Evans")
    actores.add(Chris_Evans)
    Liam_Neeson = db.nodes.create(nombreAct="Liam Neeson")
    actores.add(Liam_Neeson)
    Ewan_McGregor = db.nodes.create(nombreAct="Ewan McGregor")
    actores.add(Ewan_McGregor)
    Hayden_Christensen = db.nodes.create(nombreAct="Hayden Christensen")
    actores.add(Hayden_Christensen)
    Mark_Hamill = db.nodes.create(nombreAct="Mark Hamill")
    actores.add(Mark_Hamill)
    Carrie_Fisher = db.nodes.create(nombreAct="Carrie Fisher")
    actores.add(Carrie_Fisher)
    Harrison_Ford= db.nodes.create(nombreAct="Harrison Ford")
    actores.add(Harrison_Ford)
    Daisy_Ridley = db.nodes.create(nombreAct="Daisy Ridley")
    actores.add(Daisy_Ridley)
    Cary_Elwes = db.nodes.create(nombreAct="Cary Elwes")
    actores.add(Cary_Elwes)
    Tobin_Bell = db.nodes.create(nombreAct="Tobin Bell")
    actores.add(Tobin_Bell)
    Shawnee_Smith = db.nodes.create(nombreAct="Shawnee Smith ")
    actores.add(Shawnee_Smith)
    Costas_Mandylor = db.nodes.create(nombreAct="Costas Mandylor")
    actores.add(Costas_Mandylor)
    Scott_Patterson = db.nodes.create(nombreAct="Scott Patterson")
    actores.add(Scott_Patterson)
    Betsy_Russell  = db.nodes.create(nombreAct="Betsy Russell")
    actores.add(Betsy_Russell)
    Sean_Patrick = db.nodes.create(nombreAct="Sean Patrick")
    actores.add(Sean_Patrick)
    Jaeden_Lieberher = db.nodes.create(nombreAct="Jaeden Lieberher")
    actores.add(Jaeden_Lieberher)
    Leonardo_DiCaprio = db.nodes.create(nombreAct="Leonardo DiCaprio")
    actores.add(Leonardo_DiCaprio)
    Tom_Hanks = db.nodes.create(nombreAct="Tom Hanks")
    actores.add(Tom_Hanks)
    Al_Pacino = db.nodes.create(nombreAct="Al Pacino")
    actores.add(Al_Pacino)
    Adrien_Brody = db.nodes.create(nombreAct="Adrien Brody")
    actores.add(Adrien_Brody)
    Richard_Gere = db.nodes.create(nombreAct="Richard Gere")
    actores.add(Richard_Gere)
    Russell_Crowe = db.nodes.create(nombreAct="Russell Crowe")
    actores.add(Russell_Crowe)
    Adam_Sandler = db.nodes.create(nombreAct="Adam Sandler")
    actores.add(Adam_Sandler)
    Bradley_Cooper = db.nodes.create(nombreAct="Bradley Cooper")
    actores.add(Bradley_Cooper)
    Anna_Faris = db.nodes.create(nombreAct="Anna Faris")
    actores.add(Anna_Faris)
    Jonah_Hill = db.nodes.create(nombreAct="Jonah Hill")
    actores.add(Jonah_Hill)
    Ryan_Gosling = db.nodes.create(nombreAct="Ryan Gosling")
    actores.add(Ryan_Gosling)
    Emma_Stone = db.nodes.create(nombreAct="Emma Stone")
    actores.add(Emma_Stone)
    Channing_Tatum = db.nodes.create(nombreAct="Channing Tatum")
    actores.add(Channing_Tatum)
    Kristen_Stewart = db.nodes.create(nombreAct="Kristen Stewart")
    actores.add(Kristen_Stewart)
    John_Travolta = db.nodes.create(nombreAct="John Travolta")
    actores.add(John_Travolta)
    Zack_Efron = db.nodes.create(nombreAct="Zack Efron")
    actores.add(Zack_Efron)

    
    #Relaciones programadas
    accion.relationships.create("pertenece", deadpool)
    comedia.relationships.create("pertenece", deadpool)
    comedia.relationships.create("pertenece", deadpool_2)
    Ryan_Reynolds.relationships.create("actua", deadpool)
    accion.relationships.create("pertenece", deadpool_2)
    Ryan_Reynolds.relationships.create("actua", deadpool_2)
    accion.relationships.create("pertenece", avengers)
    Chris_Evans.relationships.create("actua", avengers)
    accion.relationships.create("pertenece", avengers2)
    Chris_Evans.relationships.create("actua", avengers2)
    accion.relationships.create("pertenece", avengers3)
    Chris_Evans.relationships.create("actua", avengers3)
    accion.relationships.create("pertenece", starw1)
    ficcion.relationships.create("pertenece", starw2)
    ficcion.relationships.create("pertenece", starw3)
    ficcion.relationships.create("pertenece", starw4)
    ficcion.relationships.create("pertenece", starw5)
    ficcion.relationships.create("pertenece", starw6)
    ficcion.relationships.create("pertenece", starw7)
    ficcion.relationships.create("pertenece", starw8)
    Liam_Neeson.relationships.create("actua", starw1)
    accion.relationships.create("pertenece", starw2)
    Ewan_McGregor.relationships.create("actua", starw2)
    accion.relationships.create("pertenece", starw3)
    Hayden_Christensen.relationships.create("actua", starw3)
    accion.relationships.create("pertenece", starw4)
    Mark_Hamill.relationships.create("actua", starw4)
    accion.relationships.create("pertenece", starw5)
    Mark_Hamill.relationships.create("actua", starw5)
    Mark_Hamill.relationships.create("actua", starw6)
    Mark_Hamill.relationships.create("actua", starw7)
    Mark_Hamill.relationships.create("actua", starw8)
    accion.relationships.create("pertenece", starw6)
    Harrison_Ford.relationships.create("actua", starw4)
    Harrison_Ford.relationships.create("actua", starw5)
    Harrison_Ford.relationships.create("actua", starw6)
    Harrison_Ford.relationships.create("actua", starw7)
    accion.relationships.create("pertenece", starw7)
    Daisy_Ridley.relationships.create("actua", starw7)
    accion.relationships.create("pertenece", starw8)
    Carrie_Fisher.relationships.create("actua", starw8)
    terror.relationships.create("pertenece", saw1)
    Cary_Elwes.relationships.create("actua", saw1)
    terror.relationships.create("pertenece", saw2)
    Tobin_Bell.relationships.create("actua", saw2)
    terror.relationships.create("pertenece", saw3)
    Shawnee_Smith.relationships.create("actua", saw3)
    terror.relationships.create("pertenece", saw4)
    Costas_Mandylor.relationships.create("actua", saw4)
    terror.relationships.create("pertenece", saw5)
    Scott_Patterson.relationships.create("actua", saw5)
    terror.relationships.create("pertenece", saw6)
    Betsy_Russell.relationships.create("actua", saw6)
    terror.relationships.create("pertenece", saw7)
    Sean_Patrick.relationships.create("actua", saw7)
    terror.relationships.create("pertenece", it)
    Jaeden_Lieberher.relationships.create("actua", it)
    drama.relationships.create("pertenece", titanic)
    Leonardo_DiCaprio.relationships.create("actua", titanic)
    drama.relationships.create("pertenece", padrino1)
    Al_Pacino.relationships.create("actua", padrino1)
    drama.relationships.create("pertenece", padrino2)
    Al_Pacino.relationships.create("actua", padrino2)
    drama.relationships.create("pertenece", padrino3)
    Al_Pacino.relationships.create("actua", padrino3)
    drama.relationships.create("pertenece", forrest)
    Tom_Hanks.relationships.create("actua", forrest)
    drama.relationships.create("pertenece", pianista)
    Adrien_Brody.relationships.create("actua", pianista)
    drama.relationships.create("pertenece", hachiko)
    Richard_Gere.relationships.create("actua", hachiko)
    drama.relationships.create("pertenece", gladiador)
    Russell_Crowe.relationships.create("actua", gladiador)
    comedia.relationships.create("pertenece", click)
    Adam_Sandler.relationships.create("actua", click)
    comedia.relationships.create("pertenece", ninos1)
    Adam_Sandler.relationships.create("actua", ninos1)
    comedia.relationships.create("pertenece", ninos2)
    Adam_Sandler.relationships.create("actua", ninos2)
    comedia.relationships.create("pertenece", zohan)
    Adam_Sandler.relationships.create("actua", zohan)
    comedia.relationships.create("pertenece", scary1)
    Anna_Faris.relationships.create("actua", scary1)
    comedia.relationships.create("pertenece", scary2)
    Anna_Faris.relationships.create("actua", scary2)
    comedia.relationships.create("pertenece", scary3)
    Anna_Faris.relationships.create("actua", scary3)
    comedia.relationships.create("pertenece", scary4)
    Anna_Faris.relationships.create("actua", scary4)
    comedia.relationships.create("pertenece", scary5)
    Anna_Faris.relationships.create("actua", scary5)
    comedia.relationships.create("pertenece", superbad)
    Jonah_Hill.relationships.create("actua", superbad)
    comedia.relationships.create("pertenece", hangover1)
    Bradley_Cooper.relationships.create("actua", hangover1)
    comedia.relationships.create("pertenece", hangover2)
    Bradley_Cooper.relationships.create("actua", hangover2)
    comedia.relationships.create("pertenece", hangover3)
    Bradley_Cooper.relationships.create("actua", hangover3)
    romance.relationships.create("pertenece", notebook)
    Ryan_Gosling.relationships.create("actua", notebook)
    romance.relationships.create("pertenece", lalala)
    Ryan_Gosling.relationships.create("actua", lalala)
    Emma_Stone.relationships.create("actua", lalala)
    romance.relationships.create("pertenece", dear)
    Channing_Tatum.relationships.create("actua", dear)
    romance.relationships.create("pertenece", primera)
    Adam_Sandler.relationships.create("actua", primera)
    romance.relationships.create("pertenece", crepusculo)
    Kristen_Stewart.relationships.create("actua", crepusculo)
    musical.relationships.create("pertenece", high1)
    Zack_Efron.relationships.create("actua", high1)
    musical.relationships.create("pertenece", high2)
    Zack_Efron.relationships.create("actua", high2)
    musical.relationships.create("pertenece", high3)
    Zack_Efron.relationships.create("actua", high3)
    musical.relationships.create("pertenece", grease)
    John_Travolta.relationships.create("actua", grease)
    
    
    
    


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
    pel = input("Ingrese el nombre de la pelicula: ")
    pelicula = db.nodes.create(nombrePel=pel)
    peliculas.add(pelicula)
#Funcion para agregar Actor
def ingresarAct():
    act = input("Ingrese el nombre del actor: ")
    actor = db.nodes.create(nombreAct=act)
    actores.add(actor)
#Gustavo este es el que hay que cambiar para que sea alreves
#Funcion para relacionar peliculas con generos
def relacionPel_Gen():
     genero = input("Ingrese el genero: ")
     peli = input("Ingrese la pelicula: ")
     try: 
         
         
         (generos.get(nombreGen=genero)[0]).relationships.create("pertenece", peliculas.get(nombrePel=peli)[0])
        
     except:
         print("No existe algun genero o pelicula o esta mal escrito")
         print(" ")
         print(" ")
#Funcion para relacionar actores con pelicula
def relacionAct_Pel():
     act1 = input("Ingrese el actor: ")
     pel2 = input("Ingrese la pelicula: ")
     try: 
         (actores.get(nombreAct=act1)[0]).relationships.create("actua", peliculas.get(nombrePel=pel2)[0]) 
     except:
         print("No existe algun actor o pelicula o esta mal escrito")
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
         print("No hay ningun genero ingresado")
         print(" ")
         print(" ")
#Funcion para consultar actor
def consultarAct():
    
    try:
        query = "MATCH (n:Actores ) RETURN n"
        results = db.query(query, data_contents=True)
        a = results.rows
        for list in a:
            for x in list:
                print (x)
    except:
         print("No hay ningun actor ingresado")
         print(" ")
         print(" ")
#Funcion para consultar pelicula por medio de su genero
def consultarPel_Gen():
    gen3 = input("Ingrese el genero que desea buscar: ")
    try:
         query = "MATCH (p:Generos{nombreGen:'"+gen3+"'})-[:pertenece]->(d:Peliculas) return d"
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
         print("No existe ninguna pelicula con ese genero")
         print("O lo escribio mal ")
         print(" ")
#Funcion para consultar pelicula por medio de su actor    
def consultarPel_Act():
    gen4 = input("Ingrese el genero que desea buscar: ")
    try:
         query = "MATCH (p:Actores{nombreAct:'"+gen4+"'})-[:actua]->(d:Peliculas) return d"
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
         print("No existe ninguna pelicula con ese actor ")
         print("O lo escribio mal ")
         print(" ")

#Ciclo principal para menu  
opcion = 0
while (opcion != 10):
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

