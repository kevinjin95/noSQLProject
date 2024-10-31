from connection import connection_redis
import json
import matplotlib.pyplot as plt
import pandas as pd
import csv

r = connection_redis()

def retrieve():
  myDict = {}
  libelle = []
  with open('files/politique/diplomesdepartements.csv') as numbers:
    numbers_data = csv.reader(numbers, delimiter=',')
    for row in numbers_data:
      libelle = row
      break
    # next(numbers_data)
    for row in numbers_data:
        values = row
        myDict2 = {}
        for ind in range(len(values)-1):
            myDict2.update({libelle[ind]: str(values[ind])})
            # print(libelle[ind])
        myDict.update({row[0]: myDict2})
    # print(myDict)
    return myDict

def dictToJson(fileName, dict):
    otfile = open(fileName, "w")
    json.dump(dict, otfile)
    otfile.close()

def jsonToRedis():
    with open("diplomesdepartements.json") as access_json:
        data = json.load(access_json)
        for key in data:
            # print(data[key])
            r.json().set(key, ".", data[key])
            # r.json().set(dict["dep"], ".", data)

def display():
    deps = r.keys("*")
    deps = sorted(deps, reverse=False)
    print(deps)
    row = []
    for dep in deps:
        row.append(r.json().get(dep, 'conjnosif1871'))
    # print(row)
    plt.scatter(deps, row)
    plt.grid(False)
    plt.title('conjnosif1871')
    # print(pd.DataFrame(row, deps))
    plt.show()

dict = {}
fileName = "diplomesdepartements.json"
# dict = retrieve()
# print(dict)
# dictToJson(fileName, dict)
# jsonToRedis()
display()

def test():
    num = [i for i in range(1, 13)]
    dict2 = {}
    # print(num)
    for i in num:
        dict = {}
        for i2 in num:
            # print(dict)
            # print(num[i-1])
            dict.update({i2 : num[i-1]})
        print("dict1:", dict)
        print("dict2:", dict2)
        dict2.update({i : dict})
    print(dict2)
