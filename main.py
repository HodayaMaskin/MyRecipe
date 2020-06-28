import pymongo

#Connect to the DB
myclient = pymongo.MongoClient("mongodb://193.106.55.98:5000/")

#use DB
mydb = myclient["RecipeForMe"]
#specific collection name
mycol = mydb["ingredients"]
#Create a dictionary and add to the Collection
mydict = {}#{ "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
y = mycol.find_one()
print("hello world - commit 2")
print("hello world - commit 3")