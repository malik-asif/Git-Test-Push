import pymongo


client = pymongo.MongoClient("mongodb+srv://malikasif:Mongo123@cluster0.bmwkqjp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    'name': 'malik aahil',
    'class': 'UKG',
    'school': 'Silver bell School'
}
db1 = client['mongotest']
coll = db1['test']

coll.insert_one(d)