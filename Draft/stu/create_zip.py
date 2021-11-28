import shutil
import zipfile
import os
from django.conf import settings


def create_file_namelist(stuid, allfile_url, downs):
    file_name = []
    for file_type, name in downs.items():
        name_1 = stuid + '-' + name
        file_url = os.path.join(allfile_url, str(file_type), name_1)
        file_name.append(file_url)
    return file_name


def create_downurl():
    down_zip = "/215_down"
    if not os.path.isdir(down_zip):
        os.mkdir(down_zip)
    down_zip = "/215_down/download_lvzhou"
    if not os.path.isdir(down_zip):
        os.mkdir(down_zip)
    return down_zip


def create_zip(stuid, stu_name, allfile_url, downs):
    zip_name = str(stuid) + stu_name + '.zip'
    file_namelist = create_file_namelist(stuid, allfile_url, downs)
    zip_file = zipfile.ZipFile(zip_name, 'w')
    for i in file_namelist:
        zip_file.write(i, os.path.basename(i), compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()
    down_zip = create_downurl()
    a = os.getcwd()
    a1 = os.path.join(a, zip_name)
    shutil.copyfile(a1, os.path.join(down_zip, zip_name))
    os.remove(a1)
    return os.path.join(down_zip, zip_name)
