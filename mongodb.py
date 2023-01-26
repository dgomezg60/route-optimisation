import pymongo as pm


class DataBase:
    def __init__(self):
        self.__url__ = 'mongodb+srv://amg:amg12@cluster0.tkycjkh.mongodb.net/?retryWrites=true&w=majority'

    def loggin(self):
        self.client = pm.MongoClient(self.__url__)
        self.db = self.client['Point']

    def get_db_names(self):
        print(self.client.list_database_names())

    def get_collection_names(self):
        print(self.db.list_collection_names())

    def __create_db__(self,name):
        self.db = self.client[f'{name}']

    def __create_collection__(self,name):
        self.col = self.db[f'{name}']
    
    def add_data(self,data):
        self.col.insert_many(data)

    def get_data(self):
        dataframe= self.col.find({})
        data = []
        for point in dataframe:
            data.append(point)
        return data

    def define_db(self,db_name,collection_name):
        self.db = self.client[f'{db_name}']
        self.col = self.db[f'{collection_name}']

