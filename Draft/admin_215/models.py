from django.db import models
from django.contrib import admin


class Admin215(models.Model):
    admin_id = models.CharField(max_length=12, primary_key=True, verbose_name='管理员学号')
    yb_realname = models.CharField(max_length=10, null=False, verbose_name='姓名')

    class Meta:
        db_table = 'admin215'
        verbose_name = 'admin'
        verbose_name_plural = 'admins'


admin.site.register(Admin215)
