from django.conf import settings
from django.core.files.storage import Storage


class FdfsStorage(Storage):
    def open(self, name, mode='rb'):
        pass

    def save(self, name, content, max_length=None):
        pass

    def url(self, name):
        return settings.FDFS_URL + name
