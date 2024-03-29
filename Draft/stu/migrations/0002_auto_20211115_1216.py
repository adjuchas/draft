# Generated by Django 3.2.7 on 2021-11-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuupload',
            name='upload_state',
            field=models.CharField(choices=[('待审核', '待审核'), ('审核通过,待征稿', '审核通过,待征稿'), ('审核不通过', '审核不通过'), ('已被征稿', '已被征稿')], default='待审核', max_length=10, null=True, verbose_name='作品状态'),
        ),
        migrations.AlterUniqueTogether(
            name='stuupload',
            unique_together={('recode_id', 'stuid', 'upload_type')},
        ),
    ]
