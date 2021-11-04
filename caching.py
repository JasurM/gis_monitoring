from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'RedisCache', 
"CACHE_REDIS_HOST" : "127.0.0.1",
"CACHE_REDIS_PASSWORD" : "o030101"})