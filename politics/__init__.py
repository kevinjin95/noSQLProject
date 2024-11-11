from politics.commons import *
from politics.to_fromMongo import *
from politics.to_fromRedis import *

def runWithMongo():
    rowName = 'conjnosif1686'
    title = 'nombre de contrat non signé dans les différents départements de france chez les femmes en 1686'
    dict = {}
    csvFile = "/home/jk1234/Documents/nouvelleBD/newDB/politics/files/csv/diplomesdepartements.csv"
    jsonFile = "/home/jk1234/Documents/nouvelleBD/newDB/politics/files/json/diplomesdepartements.json"    
    dict = csvToDict(csvFile)
    dictToJson(jsonFile, dict)
    jsonToMongo(jsonFile)
    deps, row = retrieveToMongo(rowName)
    pandaDf = reUnitToPanda1(deps, row)
    pandaDf, label = sklTest(pandaDf)
    depsList, valuesList, label = difcentroids(pandaDf)
    pandaDf, label = reUnitToPanda2(depsList, valuesList, label)
    displayClusters(pandaDf, label, title)

def runWithRedis():
    rowName = 'conjnosif1686'
    title = 'nombre de contrat non signé dans les différents départements de france chez les femmes en 1686'
    dict = {}
    csvFile = "/home/jk1234/Documents/nouvelleBD/newDB/politics/files/csv/diplomesdepartements.csv"
    jsonFile = "/home/jk1234/Documents/nouvelleBD/newDB/politics/files/json/diplomesdepartements.json"
    dict = csvToDict(csvFile)
    dictToJson(jsonFile, dict)
    jsonToRedis(jsonFile)
    deps, row = retrieveToRedis(rowName)
    deps, row = sort(deps, row)
    pandaDf = reUnitToPanda1(deps, row)
    pandaDf, label = sklTest(pandaDf)
    depsList, valuesList, label = difcentroids(pandaDf)
    pandaDf, label = reUnitToPanda2(depsList, valuesList, label)
    displayClusters(pandaDf, label, title)
