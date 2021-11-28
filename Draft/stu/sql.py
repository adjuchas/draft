from django.db import connection
from django.conf import settings
import json


class StuSql:
    def __init__(self):
        self.select_myself_sql = 'select * from stu_upload where stuid = %s and upload_type = %s;'
        self.insert_file_sql = 'insert into stu_upload (stuid, upload_name, upload_type, upload_state, create_time) ' \
                               'values (%s, %s, %s, "待审核", NOW());'
        self.find_to_delete = 'select upload_name from stu_upload where stuid = %s and upload_type = %s;'
        self.select_download_sql = 'select upload_type, upload_name from stu_upload ' \
                                   'where stuid = %s and recode_id = %s;'

    def select_self_all(self, stuid):
        recode_list = ['stuid', 'recode_id', 'upload_name', 'upload_type', 'upload_state', 'create_time']
        all_recode = []
        recodes_list = []
        with connection.cursor() as connect:
            for key in settings.LVZHOU:
                connect.execute(self.select_myself_sql, [stuid, key])
                select_1 = connect.fetchall()
                if select_1:
                    all_recode.append(select_1[-1])
        for recode in all_recode:
            recode = list(recode)
            recode[3] = settings.LVZHOU[str(recode[3])]
            recode[-1] = str(recode[-1])
            recode_1 = dict(zip(recode_list, recode))
            recodes_list.append(recode_1)
        recodes_list = list(reversed(sorted(recodes_list, key=lambda x: x['create_time'])))
        return recodes_list

    def insert_file(self, stuid, file_name, filetype):
        with connection.cursor() as connect:
            isinsert = connect.execute(self.insert_file_sql, [stuid, file_name, filetype])  # 这里会返回一个1
            return isinsert

    def find_last(self, stuid, upload_type):
        with connection.cursor() as connect:
            connect.execute(self.find_to_delete, [stuid, upload_type])
            select_1 = connect.fetchall()
            if len(select_1) < 2:
                return None
            else:
                return select_1[-2][0]

    def downloads(self, recodes, stuid):
        downs = {}
        with connection.cursor() as connect:
            for value in recodes:
                connect.execute(self.select_download_sql, [stuid, value])
                select_1 = connect.fetchone()
                if select_1:
                    downs[select_1[0]] = select_1[1]
        if downs:
            return downs
        else:
            return None
