import os
import time

from dailyfresh import settings

import django
from django.core.mail import send_mail
from celery import Celery

# celery 需要先引入当前 django 的环境以获取一些设置，因此需要添加以下代码。
# 而且当 celery 与当前项目不在同一设备时，celery 设备需要有一份相同的整个项目代码以获取设置
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailyfresh.settings')
django.setup()

# celery 运行命令
#  celery -A celery_tasks.tasks worker -l info

# 创建一个 Celery 类的对象
app = Celery('celery_tasks.tasks', broker='redis://192.168.1.5:6379/8')


# 定义任务函数
@app.task
def send_activate_mail(to, username, token):
    subject = "欢迎注册天天生鲜"
    message = ""
    sender = settings.EMAIL_FROM
    receiver = [to]
    url = f"http://127.0.0.1:8000/user/activate/{token}"
    html_message = fr"f<h1>{username}，欢迎您成为天天生鲜注册会员</h1>请点击以下链接激活您的账号\n<a href={url}>{url}</a>"
    send_mail(subject, message, sender, receiver, html_message=html_message)
    time.sleep(5)