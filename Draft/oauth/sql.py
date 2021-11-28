from django.db import connection


class InfoSql:

    def __init__(self):
        self.insert_stu = 'insert into stu_info ' \
                          '(yb_stuid, yb_realname, yb_id, create_time, yb_classname, yb_collegename) ' \
                          'value(%s, %s, %s, NOW(), %s, %s);'
        self.select_stu = 'select yb_stuid from stu_info where yb_stuid = %s;'
        self.select_admin = 'select admin_id from admin215 where admin_id = %s;'

    def ifinsertstu(self, info):
        with connection.cursor() as connect:
            connect.execute(self.select_stu, [info['stuid']])
            select_1 = connect.fetchone()
            if select_1:
                pass
            else:
                connect.execute(self.insert_stu, [info['stuid'], info['name'], info['yb_id'], info['yb_classname'],
                                                  info['collage_name']])

    def isadmin(self, stuid):
        with connection.cursor() as connect:
            connect.execute(self.select_admin, [stuid])
            select_1 = connect.fetchone()
            if select_1:
                return True
            else:
                return False
