from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.conf import settings
from .md5_obj import Md5Str
from .oauth import YbOauth
from .sql import InfoSql
from connect_redis import redis_oauth
import json


def callback_code(request):
    try:
        if request.method == 'GET':
            state = request.GET.get('state', None)
            code = request.GET.get('code', None)
            if state and code:
                yb_client = YbOauth()
                access_token = yb_client.get_access_token(code=code)
                if access_token:
                    md5obj = Md5Str()
                    new_state = md5obj.getstr(text=state)
                    isin = redis_oauth.check_havetoken(access_token=access_token)
                    connect_sql = InfoSql()
                    if isin:
                        info = redis_oauth.get_redisinfo(access_token=access_token)
                        stuid = info['stuid']
                    else:
                        info = yb_client.getinfo(access_token=access_token)
                        stuid = info['stuid']
                        connect_sql.ifinsertstu(info=info)
                    redis_oauth.set_accesstoken(state=new_state, access_token=access_token, info=str(info))  # is bool
                    isadmin = connect_sql.isadmin(stuid=stuid)
                    if isadmin:
                        url = 'https://csxy-yiban.cn/pages/215_admin/'
                        return HttpResponseRedirect(url)
                    else:
                        url = 'https://csxy-yiban.cn/pages/215/'
                        return HttpResponseRedirect(url)
        return JsonResponse(settings.ERROR)
    except Exception as e:
        print(e)


def get_accesstoken(request):
    try:
        if request.method == 'GET':
            md5uid = request.GET.get('uid', None)
            if md5uid:
                md5obj = Md5Str()
                state = str(md5obj.getstr(text=md5uid))
                access_token = redis_oauth.get_redisaccesstoken(state=state)
                if access_token:
                    return JsonResponse({
                        "message": "success",
                        "access_token": str(access_token, 'utf-8')
                    })
        return JsonResponse(settings.ERROR)
    except Exception as e:
        print(e)


def get_info(request):
    try:
        if request.method == 'GET':
            access_token = request.GET.get('access_token', None)
            if access_token:
                info = redis_oauth.get_redisinfo(access_token=access_token)
                if info:
                    return JsonResponse({
                        "message": "success",
                        "info": info
                    })
        return JsonResponse(settings.ERROR)
    except Exception as e:
        print(e)


def logout(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            md5uid = body.get('uid', None)
            access_token = body.get('access_token', None)
            if md5uid and access_token:
                md5obj = Md5Str()
                md5uid_1 = md5obj.getstr(text=md5uid)
                yb_client = YbOauth()
                isin = redis_oauth.check_havetoken(access_token=access_token)
                if isin:
                    yb_client.remove_accesstoken(access_token=access_token)
                # redis_oauth.delete_accesstoken(access_token=access_token)
                redis_oauth.delete_uid(md5uid=md5uid_1)
                return JsonResponse({
                    "message": "success"
                })
        return JsonResponse(settings.ERROR)
    except Exception as e:
        print(e)
