import redis

POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, password='csxyyiban1228nosql', max_connections=100)
token_hash = "access_token_215"
info_hash = "info_215"
