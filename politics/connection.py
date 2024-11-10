from os import getenv
from dotenv import load_dotenv

def connectionToRedis():
    from redis import Redis as connect
    
    load_dotenv()

    return connect(
        host=getenv("REDIS_HOST"), 
        # password=getenv("REDIS_PASSWORD"),
        port=getenv("REDIS_PORT"), 
        decode_responses=True
    )

def connectionToMongo():
    from pymongo import MongoClient

    load_dotenv()

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = f"mongodb+srv://kevinjin:{getenv("MONGO_SECRET_PASS")}.mongodb.net/"
 
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
 
    # Create the database for our example (we will use the same database throughout the tutorial
    return client['politics']