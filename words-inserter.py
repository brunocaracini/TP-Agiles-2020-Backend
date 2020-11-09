import pymongo
from clases import Palabra

f = open("words.txt", 'r', errors='ignore')
words = f.readlines()
new_words = []
for word in words:
    new_words.append(Palabra(word.rstrip("\n")))

client = pymongo.MongoClient("mongodb+srv://test:1234@agiles-db.jvicy.mongodb.net/<dbname>?retryWrites=true&w=majority")

mydb = client["Ahorcado"]
mycol = mydb["Palabras"]

for word in new_words:
    mydict = { "palabra": word.getPalabra(), "dificultad": word.dificultad, "puntajeDificultad": word.puntajeDificultad}
    x = mycol.insert_one(mydict)