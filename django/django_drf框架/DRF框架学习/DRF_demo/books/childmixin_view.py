import json

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from books.models import BookInfo
from books.serializers import BookSerializer


# Create your views here.

# 拓展类子类视图使用
class BooksView(ListCreateAPIView):
    """
        获取所有和保存
    """
    queryset = BookInfo.objects.all().filter(isdelete=False)  # GenericAPIView 需要先指定当前类视图使用的查询集
    serializer_class = BookSerializer  # GenericAPIView 需要先指定当前类视图使用的序列化器


class BookView(RetrieveUpdateDestroyAPIView):
    """
        获取单一数据、更新和删除
    """
    queryset = BookInfo.objects.all()  # GenericAPIView 需要先指定当前类视图使用的查询集
    serializer_class = BookSerializer  # GenericAPIView 需要先指定当前类视图使用的序列化器
