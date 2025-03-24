from pymongo import MongoClient
import json
from pprint import pprint
#################### conect to mongodb ###################
client=MongoClient(host='localhost',port=27017)
print(client)

############# make db and collection ###################
dbStudent=client['student']
score=dbStudent['score']

############ import json file ##########################
#with open("score_information.json","r") as file1:
    #objlist=json.load(file1)
    #for obj in objlist:
        #score.insert_one(obj)
        
########################################################

#for doc in score.find({'scores':{'$elemMatch':{'type':'exam','score':{'$gt':50}}}}):
    #pprint(doc)

#for doc in score.find({'course_Code':16}):
    #pprint(doc)
    
#for doc in score.find({'$and':[{'course_Code':28},{'scores':{'$elemMatch':{'type':'homework','score':{'$lt':20}}}}]}):
    #pprint(doc)

#########################################################
#score.update_many({'scores':{'$elemMatch':{'type':'exam','score':0}}},{'$set':{'scores.$.score':10}})
#for doc in score.find():
    #pprint(doc)

########################################################
for doc in score.find({'scores':{'$elemMatch':{'type':'exam','score':{'$gt':90}}}}):
    add={'grade':'A'}
    add.update(doc)