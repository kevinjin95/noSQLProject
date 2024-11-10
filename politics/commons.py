import matplotlib.pyplot as plt
import pandas as pd
import csv
from sklearn.cluster import KMeans
import numpy as np
import json

def csvToDict(csvFile):
  myDict = {}
  libelle = []
  with open(csvFile) as numbers:
    numbers_data = csv.reader(numbers, delimiter=',')
    for row in numbers_data:
      libelle = row
      break
    for row in numbers_data:
        values = row
        myDict2 = {}
        for ind in range(len(values)-1):
            myDict2.update({libelle[ind]: str(values[ind])})
        myDict.update({row[0]: myDict2})
    return myDict

def dictToJson(jsonFile, dict):
    otfile = open(jsonFile, "w")
    json.dump(dict, otfile)
    otfile.close()


def checkFloat(val):
    try:
        float(val)
    except ValueError:
        return False
    return True

def reUnitToPanda1(dep, val):
    dataset = []
    i=0
    while True:
        if checkFloat(dep[i]):
            dataset.append([float(dep[i]), float(val[i])])
        i += 1
        if i == len(dep):
            break
    pandaDf = pd.DataFrame(dataset)
    return pandaDf

def reUnitToPanda2(dep, val, clus):
    label = np.array([clus])
    dataset = []
    i=0
    while True:
        if checkFloat(dep[i]):
            dataset.append([float(dep[i]), float(val[i]), float(clus[i])])
        i += 1
        if i == len(dep):
            break
    pandaDf = pd.DataFrame(dataset)
    return pandaDf, label

def displayData(pandaDf, rowName):
    plt.scatter(pandaDf[0], pandaDf[1])
    plt.grid(False)
    plt.title(rowName)
    plt.show()


def sklTest(pandaDf):
    a = pandaDf.values[:]
    a = np.nan_to_num(a)
    kmeans = KMeans(n_clusters=4,
                    init = "k-means++",
                    n_init=6)
    kmeans.fit(a)
    label = kmeans.labels_
    pandaDf['cluster'] = label
    pandaDf.groupby('cluster').mean()
    return pandaDf, label

def displayClusters(pandaDf, label, title):
    print(pandaDf)
    print(type(label))
    surface = 10 * 10
    plt.xlabel('départements')
    plt.ylabel('nombre de contrat de mariage signé')
    plt.title(title)
    plt.scatter(pandaDf[0], pandaDf[1], surface, label.astype(np.float64), alpha = 1)
    plt.show()

def difcentroids(pandaDf):
    depsList = [i for i in pandaDf[0]]
    valuesList = [i for i in pandaDf[1]]
    clustersList = [i for i in pandaDf['cluster']]
    centroidsVal = [[0], [0], [0], [0]]
    centroidsDep = [[0], [0], [0], [0]]
    i = 0
    for clusNum in clustersList:
        centroidsVal[clusNum].append(valuesList[i])
        centroidsDep[clusNum].append(depsList[i])
        i += 1
    for group in range(len(centroidsVal)):
        centroidsVal[group] = sum(centroidsVal[group])/(len(centroidsVal[group])-1)
        centroidsDep[group] = sum(centroidsDep[group])/(len(centroidsDep[group])-1)
    ind = len(pandaDf)
    for ind in range(len(centroidsDep)):
        depsList.append(centroidsDep[ind])
        valuesList.append(centroidsVal[ind])
        clustersList.append(4)
    return depsList, valuesList, clustersList