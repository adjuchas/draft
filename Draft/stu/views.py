from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, FileResponse
from .sql import StuSql
from connect_redis import redis_stu
from .create_zip import create_zip
import os
import json
import time


def get_selfall(request):
    try:
        if request.method == 'GET':
            access_token = request.GET.get("access_token", None)
            if access_token:
                stuid = redis_stu.get_stuid(access_token=access_token)
                if stuid:
                    sql_1 = StuSql()
                    all_recode = sql_1.select_self_all(stuid=stuid)
                    return JsonResponse({
                        "message": "success",
                        "all_recode": all_recode
                    })
        return JsonResponse(settings.ERROR)
    except Exception as e:
        print(e)


def upload_file(request):
    try:
        if request.method == 'POST':
            access_token = request.POST.get('access_token', None)
            afile = request.FILES.get('myfile', None)
            file_type = request.POST.get('file_type', None)
            if access_token and afile and file_type in settings.LVZHOU.keys():
                stuid = redis_stu.get_stuid(access_token=access_token)
                if stuid:
                    file_allname = str(stuid) + "-" + str(afile.name)
                    url_1 = settings.MEDIA_ROOT  # 获取下载（上传）的根目录
                    url_1 = os.path.join(url_1, "yibanlvzhou")
                    url_type = os.path.join(url_1, file_type)
                    if not os.path.isdir(url_type):
                        os.mkdir(url_type)
                    sql_1 = StuSql()
                    isinsert = sql_1.insert_file(stuid=stuid, file_name=afile.name, filetype=file_type)
                    if isinsert:
                        file_url = os.path.join(url_type, file_allname)
                        last_name = sql_1.find_last(stuid, file_type)
                        if last_name:
                            last_allname = str(stuid) + '-' + str(last_name)
                            url_2 = os.path.join(url_type, last_allname)
                            if os.path.exists(url_2):
                                os.remove(url_2)

                        with open(file_url, 'wb') as f:
                            for chunk in afile.chunks():
                                f.write(chunk)
                            f.close()

                        return JsonResponse({
                            "message": "success"
                        })
        return JsonResponse(settings.ERROR)
    except Exception as e:
        print(e)


def download(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            access_token = body.get("access_token", None)
            recodes = body.get("recodes", None)
            if access_token and recodes:
                stuid = redis_stu.get_stuid(access_token=access_token)
                stu_name = redis_stu.get_stu_name(access_token=access_token)
                if stuid:
                    lvzhou_url = os.path.join(settings.MEDIA_ROOT, 'yibanlvzhou')
                    stusql = StuSql()
                    downs = stusql.downloads(recodes=recodes, stuid=stuid)
                    if downs:
                        zip_url = create_zip(stuid, stu_name, lvzhou_url, downs)
                        uri = "https://csxy-yiban.cn/" + zip_url
                    else:
                        uri = None
                    return JsonResponse({
                        "message": "success",
                        "uri": uri
                    })
        return JsonResponse(settings.ERROR)
    except Exception as e:
        print(e)
