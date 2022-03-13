from django.core.files.storage import Storage
from dailyfresh import settings

from fdfs_client.client import Fdfs_client, get_tracker_conf


class FDFSStorage(Storage):
    """fast dfs文件存储类"""

    def open(self, name, mode='rb'):
        """打开文件时使用"""
        pass

    def save(self, name, content, max_length=None):
        """保存文件时使用"""
        # name:选择上传文件的名字
        # content:包含上传文件内容的 File 对象

        # 创建一个Fdfs_client对象
        tracker_conf = get_tracker_conf(settings.FDFS_CLIENT_CONF)
        client = Fdfs_client(tracker_conf)

        # 上传文件到fast dfs系统中
        res = client.upload_by_buffer(content.read())

        if res.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传文件到fast dfs失败')

        # 上传成功
        # 获取返回的文件id
        filename = res.get('Remote file_id')
        # 只能返回 str 类型, filename 为 bytes 类型(需要转换类型，不然会报错)
        return filename.decode()

    def exists(self, name):
        """判断文件是否存在"""
        return False

    def url(self, name):
        """返回访问文件的url路径"""
        return f"{settings.FDFS_URL}/{name}"