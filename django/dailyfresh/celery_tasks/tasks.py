import os
import time

from dailyfresh import settings

import django
from celery import Celery
from django.core.mail import send_mail
from django.template import loader

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


@app.task
def generate_static_index_html():
    import apps.goods.models  # 这里有一个坑就是这句引入必须放在 django 引入后边，不然会找不到，所以直接放在了这个 tasks 里面
    """产生首页静态页面"""
    """
    为什么需要产生静态的首页： 
    1. 为了减缓服务器跟数据库压力，因为某些首页的数据不是经常更改的
    2. 管理员更新了首页信息对应的表格数据时才重新生成首页静态页面    
    """
    # 获取商品的种类信息
    types = apps.goods.models.GoodsType.objects.all()

    # 获取首页轮播商品信息
    goods_banners = apps.goods.models.IndexGoodsBanner.objects.all().order_by('index')  # 根据index排序，数字小的排在前边

    # 获取首页促销活动信息
    promotion_banners = apps.goods.models.IndexPromotionBanner.objects.all().order_by('index')

    # 获取首页分类商品展示信息
    for type in types:
        # 获取 type 种类首页分类商品的图片展示信息
        image_banners = apps.goods.models.IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
        # 获取 type 种类首页分类商品的文字展示信息
        title_banners = apps.goods.models.IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

        # 动态给type增加属性，分别保存首页分类商品的图片展示信息和文字展示信息，因为 Python 是可以动态添加属性的，所以这里可以直接给 type 增加属性
        type.image_banner = image_banners
        type.title_banner = title_banners

    # 组织模板上下文
    context = {'types': types, 'goods_banners': goods_banners, 'promotion_banners': promotion_banners}

    # 返回模板
    # 1. 加载模板文件
    static_temp = loader.get_template('static_index.html')
    # 2. 渲染模板
    static_index = static_temp.render(context)

    # 生成首页对应静态文件
    save_path = os.path.join(settings.BASE_DIR, 'static/index.html')
    with open(save_path, 'w') as f:
        f.write(static_index)