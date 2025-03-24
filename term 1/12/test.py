from pymongo import MongoClient
from pprint import pprint,PrettyPrinter

client=MongoClient(host='127.0.0.1',port=27017)
print(client)

dbTest=client['test']
print(dbTest)

people=dbTest['people']
print(people)

#people.insert_one({'name':'ali','family':'ahmadi','age':35})

for db in client.list_database_names():
    print(db)

print("_"*100)

for collection in dbTest.list_collection_names():
  print(collection)

for doc in people.find():
  #pprint(doc)
  PrettyPrinter(indent=4,sort_dicts=True)
  
client.close()