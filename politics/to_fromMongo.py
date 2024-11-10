from politics.connection import connectionToMongo
import json
import csv
b = connectionToMongo()
collection_name = b["politics"]

def jsonToMongo(fileName):
    with open(fileName) as access_json:
        data = json.load(access_json)
        for key in data:
            collection_name.insert_one({key: data[key]})

dbname = connectionToMongo()
collection_name = dbname["user_1_items"]

def insertMany():
  collection_name.insert_many([item_1, item_2])

def insertOne():
  collection_name.insert_one([item_3])

def find():
  item_details = collection_name.find({"name":"Lisa Rasmussen"})
  for item in item_details:
    print(item)

def create(): 
  category_index = collection_name.create_index("category")
  collection_name.insert_one([category_index])

def retrieve():
  mydict = {}
  libelle = []
  with open('files/diplomesdepartements.csv') as numbers:
    numbers_data = csv.reader(numbers, delimiter=',')
    for row in numbers_data:
      libelle = row
      break
    next(numbers_data)
    for row in numbers_data:
      values = row
      for ind in range(len(values)-1):
        mydict.update({libelle[ind]: str(values[ind])})
        break
  print(type(mydict))
  collection_name.insert_one([mydict])
  print(mydict)
      # next(numbers_data)
  # print(mydict) 
    #     if value == row[ival]:
    #       mydict.update({value: ""})
    # return mydict
      # mylist.append(row)
    #   print(row[:1])
    #   print(row)
    # break
      # mydict.update({})
    # return mylist

# create()
# find()
# insertMany()
# insertOne()
# retrieve()