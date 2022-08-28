from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from books.models import BookInfo
from books.serializers import BookSerializer


class PageNum(PageNumberPagination):
    """
        用于视图分页的类
    """
    page_size_query_param = 'page_size'  # 指定控制每页数量的参数
    page_size = 3  # 指定每页最大返回数量


# ModelViewSet 的使用
class BooksView(ModelViewSet):
    queryset = BookInfo.objects.all().filter(isdelete=False)
    # serializer_class = BookSerializer  # 当使用 get_serializer_class 方法时，这个要禁用

    # 局部认证属性
    # authentication_classes = (BasicAuthentication, SessionAuthentication)
    # 局部权限属性
    # permission_classes = (IsAuthenticated,)

    # 局部用户限流
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]

    # 局部视图限流
    # throttle_scope = 'BooksView'  # 需要限流的视图的名称

    # 指定过滤字段
    # filterset_fields = ('btitle', 'bread')

    # 排序
    filter_backends = [OrderingFilter]  # 指定排序方法类
    ordering_fields = ('id', 'bread')  # 指定排序字段

    # 分页
    pagination_class = PageNum

    def get_serializer_class(self):
        if self.action == 'lastdata':
            return BookSerializer
        else:
            return BookSerializer

    @action(methods=['get'], detail=True)  # 用于自动生成路由的装饰器， methods 为请求方式， detail 为是否生成参数正则匹配
    def lastdata(self, request, pk):
        print(self.action)  # self.action 显示的是当前方法名称，可配合 get_serializer_class 方法使用序列化器路由
        book = self.get_object()
        ser = self.get_serializer(instance=book)
        return Response(ser.data)
