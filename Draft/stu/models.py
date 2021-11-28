from django.db import models
from django.contrib import admin


class StuInfo(models.Model):
    yb_stuid = models.CharField(max_length=12, primary_key=True, null=False, verbose_name='学号')
    yb_realname = models.CharField(max_length=10, null=False, verbose_name='姓名')
    yb_id = models.IntegerField(null=False, verbose_name='易班学号')
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    yb_classname = models.CharField(max_length=20, verbose_name="班级", null=True, default="暂无信息")
    yb_collegename = models.CharField(max_length=15, null=True, default="暂无信息", verbose_name="二级学院")

    class Meta:
        db_table = 'stu_info'
        verbose_name = 'stu'
        verbose_name_plural = 'stus'


class StuUpload(models.Model):
    stuid = models.CharField(max_length=12, null=False)
    recode_id = models.AutoField(verbose_name='记录id', primary_key=True)
    upload_name = models.CharField(max_length=30, verbose_name='文件名', null=False)

    up_type = (
        (1, 'type_1'),
        (2, 'type_2'),
        (3, 'type_3')
    )

    upload_type = models.IntegerField(verbose_name='作品类型', choices=up_type)
    states = (
        ("待审核", '待审核'),
        ("审核通过,待征稿", '审核通过,待征稿'),
        ("审核不通过", '审核不通过'),
        ("已被征稿", '已被征稿')
    )
    upload_state = models.CharField(verbose_name='作品状态', max_length=10, choices=states, null=True, default="待审核")
    create_time = models.DateTimeField(verbose_name='上传时间', auto_now=True)

    class Meta:
        db_table = 'stu_upload'
        unique_together = [['recode_id', 'stuid', 'upload_type']]
        verbose_name = 'opus'
        verbose_name_plural = verbose_name


admin.site.register(StuInfo)
admin.site.register(StuUpload)
