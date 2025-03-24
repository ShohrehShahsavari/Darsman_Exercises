from pymongo import mongoclient
client=mongoclient(host='127.0.0.1',port=27017)
# print(client)
dbFood=client['Resturent']
print(dbFood)