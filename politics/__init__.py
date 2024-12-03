from politics.commons import *
from politics.to_fromRedis import *
from politics.to_fromMongo import *
import cProfile
import pstats
import time

def runWithRedis():
    rowName = 'conjnosif1686'
    title = 'nombre de contrat non signé dans les différents départements de france chez les femmes en 1686'
    dict = {}
    csvFile = "/home/jk1234/Documents/nouvelleBD/newDB/politics/static/csv/diplomesdepartements.csv"
    jsonFile = "/home/jk1234/Documents/nouvelleBD/newDB/politics/static/json/diplomesdepartements.json"
    dict = csvToDict(csvFile)
    dictToJson(jsonFile, dict)
    with cProfile.Profile() as profile:
        jsonToRedis(jsonFile)
    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()    
    start = time.time()
    jsonToRedis(jsonFile)
    end = time.time()
    print("time for jsonToRedis: ", end - start)
    deps, row = retrieveToRedis(rowName)
    pandaDf = sort(deps, row)
    pandaDf, label = sklTest(pandaDf)
    depsList, valuesList, label = difcentroids(pandaDf)
    pandaDf, label = reUnit3In1(depsList, valuesList, label)
    displayClusters(pandaDf, label, title)

def runWithMongo():
    rowName = 'conjnosif1686'
    title = 'nombre de contrat non signé dans les différents départements de france chez les femmes en 1686'
    dict = {}
    csvFile = "/home/jk1234/Documents/nouvelleBD/newDB/politics/static/csv/diplomesdepartements.csv"
    jsonFile = "/home/jk1234/Documents/nouvelleBD/newDB/politics/static/json/diplomesdepartements.json"    
    dict = csvToDict(csvFile)
    dictToJson(jsonFile, dict)
    with cProfile.Profile() as profile:
        jsonToMongo(jsonFile)
    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()    
    deps, row = retrieveToMongo(rowName)
    pandaDf = sort(deps, row)
    pandaDf, label = sklTest(pandaDf)
    depsList, valuesList, label = difcentroids(pandaDf)
    pandaDf, label = reUnit3In1(depsList, valuesList, label)
    displayClusters(pandaDf, label, title)

