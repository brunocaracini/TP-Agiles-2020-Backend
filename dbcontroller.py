import pymongo

class DBController():

    def __init__(self):
        self.mydb = None
        self.mycol = None

    @classmethod
    def openConn(self):
        client = pymongo.MongoClient("mongodb+srv://test:1234@agiles-db.jvicy.mongodb.net/Ahorcado?retryWrites=true&w=majority")
        self.mydb = client["Ahorcado"]
        self.mycol = self.mydb["Palabras"]

    @classmethod
    def getAll(self):
        palabras = []
        for x in self.mycol.find():
            palabras.append(x['palabra'].upper())
        return palabras
    
    @classmethod
    def closeConn(self):
        self.mydb = None
        self.mycol = None
