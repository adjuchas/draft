from django.http import JsonResponse
from django.conf import settings
from connect_redis import redis_admin215
from .sql import AdminSql, isadmin
from .create_zip import create_zip, create_xlsx, create_xlsx_zip
import zipfile
import json


def selectall(request):
    try:
        if request.method == 'GET':
            access_token = request.GET.get("access_token", None)
            if access_token:
                admin_id = redis_admin215.get_adminid(access_token=access_token)
                if isadmin(admin_id=admin_id):
                    adminsql = AdminSql()
                    all_recode = adminsql.select_all()
                    return JsonResponse({
                        "message": "success",
                        "recodes": all_recode
                    })
        return JsonResponse(settings.ERROR)
    except Exception as e:
        print(e)


def type_select(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            access_token = body.get('access_token', None)
            select_types = body.get('select_type', None)
            if access_token and select_types:
                admin_id = redis_admin215.get_adminid(access_token=access_token)
                if isadmin(admin_id=admin_id):
                    adminsql = AdminSql()
                    type_recode_list = []
                    for types in select_types:
                        type_recode = adminsql.select_type(file_type=types[-1])
                        type_recode_list += type_recode
                    # all_return = json.dumps(type_recode_list)
                    return JsonResponse({
                        "message": "success",
                        "recodes": type_recode_list
                    })
        return JsonResponse(settings.ERROR)
    except Exception as e:
        print(e)


def set_state(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            access_token = body.get('access_token', None)
            set_recodes = body.get('set_recode', None)
            if access_token and set_recodes:
                admin_id = redis_admin215.get_adminid(access_token=access_token)
                if isadmin(admin_id=admin_id):
                    adminsql = AdminSql()
                    isupdate = adminsql.set_state(recode_state=set_recodes)
                    if isupdate:
                        return JsonResponse({
                            "message": "success"
                        })
        return JsonResponse(settings.ERROR)
    except Exception as e:
        print(e)


def downloads(request):
    try:
        if request.method == "POST":
            body = json.loads(request.body)
            access_token = body.get('access_token', None)
            recodes = body.get("recodes", None)
            if access_token and recodes:
                admin_id = redis_admin215.get_adminid(access_token=access_token)
                if isadmin(admin_id=admin_id):
                    adminsql = AdminSql()
                    all_recode = adminsql.download_recode(recodes=recodes)
                    uri = create_zip(all_recode)
                    uri = "https://csxy-yiban.cn/" + uri
                    return JsonResponse({
                        "message": "success",
                        "uri": uri
                    })
        return JsonResponse(settings.ERROR)
    except Exception as e:
        print(e)


# 这里的下载位置好像还有问题，暂时不提供服务吧
def state_classify(request):
    try:
        if request.method == 'GET':
            access_token = request.GET.get('access_token', None)
            admin_id = redis_admin215.get_adminid(access_token=access_token)
            if isadmin(admin_id=admin_id):
                xlsx_list = []
                adminsql = AdminSql()
                for key, value in settings.DRAFT_STATES.items():
                    select_1 = adminsql.state_classify(value)
                    xlsx_name = create_xlsx(value, select_1)
                    xlsx_list.append(xlsx_name)
                uri = create_xlsx_zip(xlsx_list)
                uri = "https://csxy-yiban.cn/" + uri
                return JsonResponse({
                    "message": "success",
                    "uri": uri
                })
        return JsonResponse(settings.ERROR)
    except Exception as e:
        print(e)
