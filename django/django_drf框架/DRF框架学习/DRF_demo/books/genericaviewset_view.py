import json

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet

from books.models import BookInfo
from books.serializers import BookSerializer


# Create your views here.

# 视图集使用
class BooksView(GenericViewSet):
    """
        获取所有和保存
    """
    queryset = BookInfo.objects.all().filter(isdelete=False)
    serializer_class = BookSerializer

    def list(self, request):  # Viewset 的方法不再按照请求方式写，而是用普通方法名

        # 1. 查询所有图书对象
        books = self.get_queryset()

        # 2. 返回图书数据
        # 使用序列化器
        ser = self.get_serializer(books, many=True)
        return Response(ser.data)

    def create(self, request):
        # 1. 获取前端数据
        data_dict = request.data  # 继承 ref apiview 之后，request 获取数据的方式要改变
        # 2. 验证数据
        # 序列化器验证数据
        ser = self.get_serializer(data=data_dict)
        ser.is_valid(raise_exception=True)
        print(ser.validated_data)

        # 3. 保存数据
        # 序列化器保存
        ser.save()

        # 4. 返回结果
        # 序列化器返回
        return Response(ser.errors)  # 继承 ref apiview 之后，response 方法也需要改变，统一为 Response


class BookView(GenericViewSet):
    """
        获取单一数据、更新和删除
    """
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer

    def lastdata(self, request, pk):  # 获取单一数据
        # 1. 查询数据对象
        book = self.get_object()
        print(book)

        # 使用序列化器
        ser = self.get_serializer(instance=book)
        return Response(ser.data)

    def update(self, request, pk):  # 更新
        print("当前方法为 update ")
        # 1. 获取前端数据
        data_dict = request.data
        print(data_dict)

        # 序列化器更新操作
        # 2. 验证数据
        try:
            book = self.get_object()
            print(book)
        except:
            return Response({'error': '错误信息'}, status=400)

        ser = self.get_serializer(book, data=data_dict)
        ser.is_valid()

        # 3. 更新数据
        ser.save()

        # 4. 返回数据
        return Response(ser.data)

    def delete_view(self, request, pk):  # 删除
        # 1. 查询数据对象
        try:
            book = self.get_object()
        except:
            return Response({'error': '错误信息'}, status=400)

        book.isdelete = True
        book.save()
        return Response({})
