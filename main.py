from politics.__init__ import runWithRedis, runWithMongo

if __name__ == '__main__':
    runWithMongo()
    runWithRedis()