from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from books.models import BookInfo
from books.serializers import BookSerializer


# ModelViewSet 的使用
class BooksView(ModelViewSet):
    queryset = BookInfo.objects.all().filter(isdelete=False)
    serializer_class = BookSerializer

    @action(methods=['get'], detail=True)  # 用于自动生成路由的装饰器， methods 为请求方式， detail 为是否生成参数正则匹配
    def lastdata(self, request, pk):
        book = self.get_object()
        ser = self.get_serializer(instance=book)
        return Response(ser.data)
