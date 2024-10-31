def connection_redis():
    from redis import Redis as connect
    from os import getenv
    from dotenv import load_dotenv

    load_dotenv()

    return connect(
        host=getenv("REDIS_HOST"), 
        # password=getenv("REDIS_PASSWORD"),
        port=getenv("REDIS_PORT"), 
        decode_responses=True
    )
