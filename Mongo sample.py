import pymongo
client = pymongo.MongoClient()

mydb = client["mydb"]
mycol = mydb["people"]
#Create a collection
datalist = [{"name":"brian", "age":40},{"name":"mark"}]
x = mycol.insert_many(datalist)

print(x.inserted_ids)
mydb = client["mydb"]

##Check all the databases
print(mydb.list_collection_names())

mycol = mydb["Employee"]

#Print all documents
for x in mycol.find():
    print(x)

#select all department under HR
for x in mycol.find({"Department":"HR"}):
    print(x)

# fields to show, projections works
for x in mycol.find({"Department":"HR"},{"EmpID":1,"EmpFname":1}):
    print(x)

# Find all employees under P1 project
for x in mycol.find({"Project":"P1"},{"EmpFname":1}):
    print(x)

mycol.find( {"EmpFname": { $regex: /s/ } } )
#Pattern Match
for x in mycol.find( {"EmpFname": { $regex: /s/ } } ):
   print(x)
