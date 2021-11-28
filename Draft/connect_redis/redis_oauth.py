from .connect_pool import POOL, token_hash, info_hash
import redis
import json


def set_accesstoken(state, access_token, info):
    conn = redis.Redis(connection_pool=POOL)
    pipe = conn.pipeline()
    pipe.hset(token_hash, str(state), access_token)
    pipe.hset(info_hash, access_token, info)
    res = pipe.execute()
    # print(res)
    # 这里的res是一个list，里面记录两条redis语句是否执行，例如[1, 0]. [1, 1],所以这里不要返回值，有需要可以打印出来看看


def check_havetoken(access_token):
    conn = redis.Redis(connection_pool=POOL)
    isin = conn.hexists(info_hash, access_token)
    return isin


def get_redisaccesstoken(state):
    conn = redis.Redis(connection_pool=POOL)
    isin = conn.hexists(token_hash, str(state))
    if isin:
        access_token = conn.hget(token_hash, state)
        return access_token
    else:
        return None


def get_redisinfo(access_token):
    conn = redis.Redis(connection_pool=POOL)
    isin = conn.hexists(info_hash, access_token)
    if isin:
        info = conn.hget(info_hash, access_token)
        info_1 = eval(info)
        return info_1
    else:
        return None


def delete_accesstoken(access_token):
    conn = redis.Redis(connection_pool=POOL)
    isin = conn.hexists(info_hash, access_token)
    if isin:
        conn.hdel(info_hash, access_token)
        return True
    else:
        return True


def delete_uid(md5uid):
    conn = redis.Redis(connection_pool=POOL)
    isin = conn.hexists(token_hash, md5uid)
    if isin:
        conn.hdel(token_hash, md5uid)
        return True
    else:
        return True
