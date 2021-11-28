from .connect_pool import POOL, info_hash
import redis


def get_adminid(access_token):
    conn = redis.Redis(connection_pool=POOL)
    isin = conn.hexists(info_hash, access_token)
    if isin:
        admin_id = eval(conn.hget(info_hash, access_token).decode())["stuid"]
        return admin_id
    else:
        return None
