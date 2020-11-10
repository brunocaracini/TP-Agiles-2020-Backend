import pymongo

class Data():

    def __init__(self):
        self.mydb = None
        self.mycol = None

    @classmethod
    def openConnPalabras(self):
        client = pymongo.MongoClient("mongodb+srv://test:1234@agiles-db.jvicy.mongodb.net/Ahorcado?retryWrites=true&w=majority")
        self.mydb = client["Ahorcado"]
        self.mycol = self.mydb["Palabras"]

    @classmethod
    def openConnRanking(self):
        client = pymongo.MongoClient("mongodb+srv://test:1234@agiles-db.jvicy.mongodb.net/Ahorcado?retryWrites=true&w=majority")
        self.mydb = client["Ahorcado"]
        self.mycol = self.mydb["Ranking"]

    @classmethod
    def getRandomWord(self, dificultad):
        self.openConnPalabras()
        for x in self.mycol.aggregate([ { "$match": { "dificultad": dificultad }}, { "$sample": { "size": 1 }}]):
            return x['palabra'].upper()
    
    @classmethod
    def getRanking(self):
        self.openConnRanking()
        mydoc = self.mycol.find().sort("puntaje",-1).limit(10)
        i = 1
        ranking = {}
        for x in mydoc:
            mydict = {"nombre": x['nombre'], "puntaje": x['puntaje']}
            ranking[i] = mydict
            i+=1
        return ranking

    @classmethod
    def actualizaRanking(self, puntaje, nombreJugador):
        self.openConnRanking()
        mydict = {"nombre": nombreJugador, "puntaje": puntaje}
        self.mycol.insert_one(mydict)