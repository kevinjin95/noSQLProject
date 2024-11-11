from politics.connection import connectionToMongo
import json

b = connectionToMongo()
collection_name = b["politics"]

def jsonToMongo(fileName):
  with open(fileName) as access_json:
    data = json.load(access_json)
    for key in data:
      collection_name.insert_one(data[key])

def retrieveToMongo(rowName):
  deps = []
  row = []
  depsNum = collection_name.find()
  for value in depsNum:
    deps.append(value["dep"])
    row.append(value[rowName])
  return deps, row