from rest_framework.generics import ListCreateAPIView

from meiduo_admin.serialziers.users import UserSerializer
from meiduo_admin.utils import PageNum
from users.models import User


class UserView(ListCreateAPIView):
    """
        获取用户数据
    """
    # 指定查询集
    queryset = User.objects.all().order_by('id')
    # 指定序列化器
    serializer_class = UserSerializer
    # 使用分页器
    pagination_class = PageNum

    def get_queryset(self):
        """
            重写 GenericAPIView 中的方法以满足 user 搜索
        """
        if self.request.query_params.get('keyword') == '':
            return User.objects.all().order_by('id')  # 搜索所用用户
        else:
            return User.objects.filter(username__contains=self.request.query_params.get('keyword')).order_by(
                'id')  # 搜索单一用户，contains 激活模糊查询
