import pymongo as pm

class MongoDB:
    def __init__(self):
        client = pm.MongoClient("localhost", 27017)
        self.db = client.test

    def update_db(self, pref, value):
        self.db.somedata.update_one({}, {"$set": {pref: value}})

    def get_info(self, pref):
        return self.db.somedata.find_one()[pref]