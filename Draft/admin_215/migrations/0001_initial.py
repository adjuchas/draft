# Generated by Django 3.2.7 on 2021-11-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin215',
            fields=[
                ('admin_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='管理员学号')),
                ('yb_realname', models.CharField(max_length=10, verbose_name='姓名')),
            ],
            options={
                'verbose_name': 'admin',
                'verbose_name_plural': 'admins',
                'db_table': 'admin215',
            },
        ),
    ]
