from haystack import indexes
from apps.goods.models import GoodsSKU


# 指定对于某个类的某些数据建立索引
# 索引类名称格式：模型类名+index
class GoodsSKUIndex(indexes.SearchIndex, indexes.Indexable):  # 默认需要继承这两个类
    # document 为 True 说明 text 是索引字段， use_template 指定根据表中哪些字段建立索引文件，把说明放在一个文件中，
    # 文件在 templates/search/indexes/模型类所在应用名字/模型类名称小写_text.txt（固定路径）
    # 在本次项目中为 templates/search/indexes/goods/goodssku_text.txt
    # 然后通过 python manage.py rebuild_index 建立索引
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        # 返回模型类
        return GoodsSKU

    # 对返回的数据建立索引
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
