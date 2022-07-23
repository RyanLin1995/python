import json

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin

from books.models import BookInfo
from books.serializers import BookSerializer


# Create your views here.

# 拓展类视图使用
class BooksView(GenericAPIView, CreateModelMixin, ListModelMixin):
    """
        获取所有和保存
    """
    queryset = BookInfo.objects.all().filter(isdelete=False)  # GenericAPIView 需要先指定当前类视图使用的查询集
    serializer_class = BookSerializer  # GenericAPIView 需要先指定当前类视图使用的序列化器

    def get(self, request):
        return self.list(request)  # 因为拓展类封装了方法，所以直接返回拓展类的方法即可

    def post(self, request):
        return self.create(request)


class BookView(GenericAPIView, UpdateModelMixin, DestroyModelMixin):
    """
        获取单一数据、更新和删除
    """
    queryset = BookInfo.objects.all()  # GenericAPIView 需要先指定当前类视图使用的查询集
    serializer_class = BookSerializer  # GenericAPIView 需要先指定当前类视图使用的序列化器

    def get(self, request, pk):  # 获取单一数据
        return self.get(request, pk)

    def put(self, request, pk):  # 更新
        return self.update(request, pk)

    def delete(self, request, pk):  # 删除
        return self.destroy(request, pk)
