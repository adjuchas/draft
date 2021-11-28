from django.db import connection
from django.conf import settings


recode_list = ['stuid', 'recode_id', 'upload_name', 'upload_type', 'upload_state', 'create_time']


def isadmin(admin_id):
    sql_ = 'select * from admin215 where admin_id = %s;'
    with connection.cursor() as connect:
        connect.execute(sql_, [admin_id])
        select_1 = connect.fetchone()
    if select_1:
        return True
    else:
        return False


def dict_zip(allrecode):
    allrecode_1 = []
    for recode in allrecode:
        recode_1 = dict(zip(recode_list, recode))
        allrecode_1.append(recode_1)
    return allrecode_1


class AdminSql:
    def __init__(self):
        self.select_all_sql = 'select * from stu_upload where recode_id in ' \
                              '(select max(recode_id) from stu_upload group by stuid, upload_type);'
        self.select_type_sql = 'select * from stu_upload where recode_id in ' \
                               '(select max(recode_id) from stu_upload group by stuid, upload_type)' \
                               'and upload_type = %s;'
        self.set_state_sql = 'update stu_upload set upload_state = %s where recode_id = %s;'
        self.download_recode_sql = 'select stuid, upload_type, upload_name from stu_upload where recode_id = %s;'
        self.state_classify_sql = 'select stuid, upload_name, upload_type, upload_state from stu_upload ' \
                                  'where recode_id in (select max(recode_id) from stu_upload ' \
                                  'group by stuid, upload_type) and upload_state = %s;'
        self.find_name = 'select yb_realname from stu_info where yb_stuid = %s;'

    def select_all(self):
        with connection.cursor() as connect:
            connect.execute(self.select_all_sql)
            allrecode = connect.fetchall()
            allrecode_list = dict_zip(allrecode)
            for i in allrecode_list:
                i["upload_type"] = settings.LVZHOU[str(i["upload_type"])]
                i["create_time"] = str(i["create_time"])
        return allrecode_list

    def select_type(self, file_type):
        with connection.cursor() as connect:
            connect.execute(self.select_type_sql, [file_type])
            type_recode = connect.fetchall()
            type_recode_list = dict_zip(type_recode)
            for recode in type_recode_list:
                recode['upload_type'] = settings.LVZHOU[str(recode['upload_type'])]
        return type_recode_list

    def set_state(self, recode_state):
        with connection.cursor() as connect:
            for recode_1 in recode_state:
                for key, value in recode_1.items():
                    connect.execute(self.set_state_sql, [value, key])
        return True

    def download_recode(self, recodes):
        all_down = {}
        with connection.cursor() as connect:
            for key in recodes:
                connect.execute(self.download_recode_sql, [key])
                select_1 = list(connect.fetchone())
                all_down[key] = select_1
        return all_down

    def state_classify(self, state):
        with connection.cursor() as connect:
            connect.execute(self.state_classify_sql, [state])
            select_1 = list(connect.fetchall())
        return select_1

    def find_names(self, stuid_list):
        name_list = []
        with connection.cursor() as connect:
            for stuid in stuid_list:
                connect.execute(self.find_name, [stuid])
                name_list.append(connect.fetchone()[0])
        return name_list
