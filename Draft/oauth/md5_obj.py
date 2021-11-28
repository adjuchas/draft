import hashlib


class Md5Str:
    def __init__(self):
        self.obj_ = hashlib.md5()
        self.md5value = None

    def getstr(self, text):
        self.obj_.update(text.encode('utf-8'))
        md5value = self.obj_.hexdigest()
        return md5value
