from .connect_pool import POOL, info_hash
import redis


def get_stuid(access_token):
    conn = redis.Redis(connection_pool=POOL)
    isin = conn.hexists(info_hash, str(access_token))
    if isin:
        info = conn.hget(info_hash, access_token).decode()
        info = eval(info)
        if info:
            return info['stuid']
        else:
            return None
    else:
        return None


def get_stu_name(access_token):
    conn = redis.Redis(connection_pool=POOL)
    isin = conn.hexists(info_hash, str(access_token))
    if isin:
        info = conn.hget(info_hash, access_token).decode()
        info = eval(info)
        if info:
            return info['name']
        else:
            return None
    else:
        return None
