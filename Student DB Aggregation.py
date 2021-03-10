import pymongo
client = pymongo.MongoClient()

db = client["mydb"]
col = db["Student"]

###########          Aggregation       ############
########  SUM ####
result = col.aggregate([{"$group":
                             {"_id":"$score",
                              "Total":{"$sum":1}
                              }}
                        ])
for i in result:
    print(i)

# Select distinct records
result = col.distinct("subject")
for i in result:
    print(i)

#### Top 5 on PlaceofBirth
result5 = col.aggregate([{"$group":
                              {"_id": "$PlaceofBirth",
                               "Total": {"$sum":1}}
                          },
                        {"$sort":
                              {"Total":-1}},
                         {"$limit":5}
                         ])
for i in result5:
    print(i)

####  Find 2nd highest Place of Birth place
result6 = col.aggregate([{"$group":
                              {"_id": "$PlaceofBirth",
                               "Total": {"$sum":1}}
                          },
                        {"$sort":
                              {"Total":-1}},
                         {"$limit":2},
                         {"$skip":1}
                         ])
for i in result6:
    print(i)

####Match
result7 = col.aggregate([{"$match":
                              {"Grade": 'G'}}])
for i in result7:
    print(i)
