from politics.connection import connectionToRedis, connectionToMongo
import json

b = connectionToRedis()

def jsonToRedis(fileName):
    with open(fileName) as access_json:
        data = json.load(access_json)
        for key in data:
            b.json().set(key, ".", data[key])

def retrieveToRedis(rowName):
    deps = b.keys("*")
    deps = sorted(deps, reverse=False)
    row = []
    for dep in deps:
        row.append(int(b.json().get(dep, rowName)))
    return deps, row
