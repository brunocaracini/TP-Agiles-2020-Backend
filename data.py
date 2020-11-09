import pymongo

class Data():

    def __init__(self):
        self.mydb = None
        self.mycol = None

    @classmethod
    def openConn(self):
        client = pymongo.MongoClient("mongodb+srv://test:1234@agiles-db.jvicy.mongodb.net/Ahorcado?retryWrites=true&w=majority")
        self.mydb = client["Ahorcado"]
        self.mycol = self.mydb["Palabras"]

    @classmethod
    def getRandomWord(self, dificultad):
        self.openConn()
        for x in self.mycol.aggregate([{ "$sample": { "size": 1 }, "dificultad": dificultad}]):
            return x['palabra'].upper()