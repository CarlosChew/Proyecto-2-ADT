"""
Gustavo De Leon  17085
Luis Esturban  17256
Carlos Chew 17507
"""

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

#Creacion de base de datos de grafos con su nombre y contraseña
db = GraphDatabase("http://localhost:7474", username="TuPeli", password="pelicula")

#cracion de nodos principales(En proceso)
generos = db.labels.create("Generos")
peliculas = db.labels.create("Peliculas")

# Generos de las Peliculas(En proceso)
terror = db.nodes.create(name="Terror")
romance = db.nodes.create(name="Romance")
accion = db.nodes.create(name="Accion")
comedia = db.nodes.create(name="Comedia")
drama = db.nodes.create(name="Drama")
ficcion = db.nodes.create(name="Ficcion")
musical = db.nodes.create(name="Musical")
suspenso = db.nodes.create(name="Suspenso")

# agregar generos (En proceso)
generos.add(terror, romance, accion, comedia, comedia, drama, ficcion, musical, suspenso)


# Creando cada pelicula (En proceso)
capitanA1 = db.nodes.create(name="Capitan America 1")
jurassic1 = db.nodes.create(name="Jurassic Park 1")
chucky1 = db.nodes.create(name= "Chucky 1")
viernes13 = db.nodes.create(name="Viernes 13")
purga = db.nodes.create(name="La Purga")
infinityW = db.nodes.create(name="Infinity War")
scaryM = db.nodes.create(name="Scary Movie")
high = db.nodes.create(name="High School Musical")
lalala = db.nodes.create(name="Lalala")
starW = db.nodes.create(name="Star Wars")
indianaJ = db.nodes.create(name="Indiana Jones")
titanic = db.nodes.create(name="Titanic")
harryP = db.nodes.create(name="Harry Potter")

#agregando las peliculas
peliculas.add(capitanA1, jurassic1, chucky1, viernes13, purga, infinityW, scaryM, high, lalala, starW, indianaJ, titanic, harryP)


#Conectando cada genero con pelicula (En proceso)
capitanA1.relationships.create("es de ",accion)
capitanA1.relationships.create("es de ",comedia)
capitanA1.relationships.create("es de ",ficcion)

jurassic1.relationships.create("es de ",accion)
jurassic1.relationships.create("es de ",ficcion)
jurassic1.relationships.create("es de ",suspenso)

chucky1.relationships.create("es de ",terror)
chucky1.relationships.create("es de ",suspenso)
chucky1.relationships.create("es de ",comedia)

viernes13.relationships.create("es de ",terror)
viernes13.relationships.create("es de ",accion)
viernes13.relationships.create("es de ",suspenso)

purga.relationships.create("es de ",suspenso)
purga.relationships.create("es de ",terror)
purga.relationships.create("es de ",drama)

infinityW.relationships.create("es de ",comedia)
infinityW.relationships.create("es de ",suspenso)
infinityW.relationships.create("es de ",accion)

scaryM.relationships.create("es de ",comedia)
scaryM.relationships.create("es de ",accion)
scaryM.relationships.create("es de ",suspenso)

high.relationships.create("es de ",musical)
high.relationships.create("es de ",romance)
high.relationships.create("es de ",comedia)

lalala.relationships.create("es de ",comedia)
lalala.relationships.create("es de ",romance)
lalala.relationships.create("es de ",drama)

starW.relationships.create("es de ",ficcion)
starW.relationships.create("es de ",accion)

indianaJ.relationships.create("es de ",accion)
indianaJ.relationships.create("es de ",ficcion)


titanic.relationships.create("es de ",drama)
titanic.relationships.create("es de ",romance)
titanic.relationships.create("es de ",suspenso)

harryP.relationships.create("es de ",ficcion)
harryP.relationships.create("es de ",accion)


