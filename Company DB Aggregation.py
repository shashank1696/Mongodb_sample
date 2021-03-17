########Company Data
import pymongo
client = pymongo.MongoClient()

db = client["mydb"]
col = db["Company"]
#Aggregation

###Return average city population
result = col.aggregate([{"$group":
                             {"_id":"$city",
                              "pop" : {"$sum":"$pop"}}},
                        {"$sort":
                            {"pop":-1}},
                         {"$limit":5}
                        ])
for i in result:
    print(i)

### Return Average city Population by state
result1 = col.aggregate([{"$group":
                             {"_id":"$state","_id":"$city",
                              "pop" : {"$sum":"$pop"}}},
                         {"$group":
                             {"_id":"$_id.state", "Avgcitypop" : {"$avg": "$pop"}}}
                        ])
for i in result1:
    print(i)
    
#Return Largest Cities by State
result2 = col.aggregate([{"$group":
                             {"_id":{"state": "$state","city":"$city"},
                              "pop" : {"$sum":"$pop"}}},
                         {"$sort":
                              {"pop":1}},
                         {"$group":
                             {"_id":"$_id.state",
                             "biggestcity": {"$last": "$_id.city"},
                              "biggestpop": {"$last": "$pop"}}
                         },
                         {"$project":
                              {"_id":0,
                               "state":"$_id",
                               "biggestcity": {"name": "$biggestcity","pop": "$biggestpop"}}}
                        ])
for i in result2:
    print(i)
