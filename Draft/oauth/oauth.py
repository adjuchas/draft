from django.conf import settings
import requests


class YbOauth:

    def __init__(self):
        self.access_token_url = 'https://openapi.yiban.cn/oauth/access_token'
        self.info_url = 'https://openapi.yiban.cn/user/verify_me'
        self.remove_token_url = 'https://openapi.yiban.cn/oauth/revoke_token'

    def get_access_token(self, code):
        data = {
            'client_id': settings.APPID,
            'client_secret': settings.APPSECRET,
            'code': code,
            'redirect_uri': settings.REDIRECTURI
        }
        response = requests.post(url=self.access_token_url, data=data)
        access_token = response.json().get('access_token', None)
        if access_token:
            return access_token
        else:
            return None

    def getinfo(self, access_token):
        params = {
            'access_token': access_token
        }

        response = requests.get(url=self.info_url, params=params).json()['info']
        try:
            info = {
                'stuid': response.get('yb_studentid', None),
                'name': response.get('yb_realname', None),
                'yb_id': response.get('yb_userid'),
                'collage_name': response.get('yb_collegename', None),
                'yb_classname': response.get('yb_classname', None)
            }
        except:
            info = {
                'stuid': '000000000000',
                'name': '测试使用',
                'yb_id': '000000',
                'collage_name': '测试使用学院',
                'yb_classname': '测试使用班级'
            }
        return info

    def remove_accesstoken(self, access_token):
        data = {
            'client_id': settings.APPID,
            'access_token': access_token
        }
        response = requests.post(url=self.remove_token_url, data=data)
        status = int(response.json()['status'])
        if status == 200:
            return True
        else:
            return False
