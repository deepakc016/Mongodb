import pymongo
client = pymongo.MongoClient("mongodb+srv://m001-student:m001-mongodb-basics@sandbox.tigcw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

#pip install pymongo

d={
    "name":"Sudhanshu",
    "email": "sudhanshu@ineuron.ai",
    "surname": "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)