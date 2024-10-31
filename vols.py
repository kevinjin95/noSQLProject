import json
from connection import connection_redis
r = connection_redis()

r.set("haha", "oops")

print(r.get("haha"))

dictAvions = {}
dictClients = {}
dictDefClasses = {}
dictPilotes = {}
dictReserv = {}
dictVols = {}

def getAvions():
    file = "AVIONS.txt"
    dictAvions = {}
    with open(file) as fn:
        for d in fn:
            key, desc = d.strip().split(None, 1)
            d_split = desc.split("\t")
            dictAvions.update({key: {
                "marqueEtModele": d_split[0], 
                "nombre": d_split[1], 
                "ville": d_split[2]
                }
            })
    return dictAvions

def getClients():
    file = "CLIENTS.txt"
    dictClients = {}
    with open(file) as fn:
        for d in fn:
            key, desc = d.strip().split(None,1)
            d_split = desc.split("\t")
            dictClients.update({key: {
                "nom": d_split[0],
                "numero": d_split[1], 
                "rue": d_split[2], 
                "code postale": d_split[3], 
                "ville": d_split[4]
                }
            })
    return dictClients

def getDefClasses():
    file = "DEFCLASSES.txt"
    dictDefClasses = {}
    with open(file) as fn:
        for d in fn:
            key, desc = d.strip().split(None, 1)
            dictDefClasses.update({key: {
                "Economique": 0,     
                "Touriste": 0, 
                "Business": 0
                }
            })
    with open(file) as fn:
        for d in fn:
            key, desc = d.strip().split(None, 1)
            d_split = desc.split("\t")
            dictDefClasses[key].update({d_split[0]: d_split[1]})
    return dictDefClasses

def getPilotes():
    file = "PILOTES.txt"
    dictPilotes = {}
    with open(file) as fn:
        for d in fn:
            key, desc = d.strip().split(None, 1)
            d_split = desc.split("\t")
            dictPilotes.update({key: {
                "nomPilote": d_split[0], 
                "anneeDeNaissance": d_split[1], 
                "villeDeNaissance": d_split[2]
                }
            })
    #print(dictPilotes)
    return dictPilotes

def getReservations():
    file = "RESERVATIONS.txt"
    dictReservations = {}
    with open(file) as fn:
        for d in fn:
            key, desc = d.strip().split(None, 1)
            d_split = desc.split("\t")
            dictReservations.update({key: {
                "vol": d_split[0], 
                "classe": d_split[1], 
                "nombreDePlaces": d_split[2]
                }
            })
    return dictReservations

def getVols():
    file = "VOLS.txt"
    dictVols = {}
    with open(file) as fn:
        for d in fn:
            key, desc = d.strip().split(None, 1)
            d_split = desc.split("\t")
            dictVols.update({key: {
                "villeDepart": d_split[0],
                "villeArrivee": d_split[1], 
                "dateDepart":d_split[2], 
                "heureDepart":d_split[3], 
                "dateArrivee":d_split[4], 
                "heureArrivee":d_split[5],
                "numeroPilote":d_split[6],
                "numeroAvion":d_split[7]
                }
            })
    #print(dictVols)
    return dictVols

def normalizeVols(dictPilotes, dictVols, dictAvions, dictReserv, dictClients, dictDefClasses):
    # print("keys of avions", list(dictAvions))
    for ind in list(dictVols):
        dictVols[ind].update(dictAvions[dictVols[ind]["numeroAvion"]]) #ajout des valeurs d'avions dans vol 
    #print(dictVols)
    # print("keys of pilotes", list(dictPilotes))
    for ind in list(dictVols):
        dictVols[ind].update(dictPilotes[dictVols[ind]["numeroPilote"]]) #ajout des valeurs de pilote dans vol 

    # #print("keys of reserv", list(dictReserv))
    for ind in list(dictReserv):
        dictReserv[ind].update(dictClients[ind]) #ajout des valeurs de clents dans reservations
      
    # #print("keys of defclasses", list(dictdefClasses))
    for ind in list(dictReserv):
        laClasse = dictReserv[ind]["classe"]
        lesClasses = dictDefClasses[dictReserv[ind]["vol"]]
        dictReserv[ind].update({"coefPrix": lesClasses.get(laClasse)}) #ajout des valeurs de clents dans reservations

def dictToJson(fileName, dict):
    otfile = open(fileName, "w")
    json.dump(dict, otfile)
    otfile.close()
    

def jsonToRedis():
    with open("reservations.json") as access_json:
        data = json.load(access_json)
        for key in data:
            r.json().set(key, ".", data[key])
    with open("vols.json") as access_json:
        data = json.load(access_json)
        for key in data:
            r.json().set(key, ".", data[key])
    
def countPilote():
    vols = r.keys("V*")
    idPilotes = []
    for ind in vols:
        if r.json().get(ind, "numeroPilote") not in idPilotes:
            idPilotes.append(r.json().get(ind, "numeroPilote"))
    print("nombre de pilotes: ", len(idPilotes))
    
def AToB(villeD):
    villeA = []
    vols = r.keys("V*")
    for ind in vols:
        if r.json().get(ind, "villeDepart") == villeD:
            if r.json().get(ind, "villeArrivee") not in villeA:
                villeA.append(r.json().get(ind, "villeArrivee"))
    return villeA
            
def main():
    #dictAvions = getAvions()
    #print(dictAvions)
    # dictPilotes = getPilotes()
    # dictVols = getVols()
    #print(dictVols)
    # dictClients = getClients()
    # dictReserv = getReservations()
    # dictDefClasses = getDefClasses()
    # normalizeVols(dictPilotes, dictVols, dictAvions, dictReserv, dictClients, dictDefClasses)
    # dictToJson("reservations.json", dictReserv)
    # dictToJson("vols.json", dictVols)
    jsonToRedis()
    #countPilote()
    villeD = "Paris"
    print(AToB(villeD))
    r.set("ffo", "1")

if __name__=="__main__": 
    main()

#data = json.load(jsonFile) a json to a dictionnary

