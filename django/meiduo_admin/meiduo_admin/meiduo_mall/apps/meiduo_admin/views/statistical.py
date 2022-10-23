from datetime import date, timedelta

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from meiduo_admin.serialziers.statistical import *
from users.models import User


class UserCountView(APIView):
    """
        用户总量统计
    """
    # 权限指定
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 1. 获取当天时间
        now_date = date.today()
        # 2. 获取用户总量
        count = User.objects.all().count()
        # 3. 返回结果
        return Response({
            'date': now_date,
            'count': count
        })


class UserDayCountView(APIView):
    """
        日增用户统计
    """
    # 权限指定
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 1. 获取当天时间
        now_date = date.today()
        # 2. 获取当天注册用户总量
        count = User.objects.filter(date_joined__gte=now_date).count()  # 这里会灵活取值
        # 3. 返回结果
        return Response({
            'date': now_date,
            'count': count
        })


class UserDayActivateView(APIView):
    """
        日增用户统计
    """
    # 权限指定
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 1. 获取当天时间
        now_date = date.today()
        # 2. 获取当天注册用户总量
        count = User.objects.filter(last_login__gte=now_date).count()  # 这里会灵活取值
        # 3. 返回结果
        return Response({
            'date': now_date,
            'count': count
        })


class UserDayOrdersCountView(APIView):
    """
        当天下单用户统计
    """
    # 权限指定
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 1. 获取当天时间
        now_date = date.today()
        # 2. 获取当天注册用户总量
        count = len(set(User.objects.filter(orders__create_time__gte=now_date)))  # 这里会灵活取值
        # 3. 返回结果
        return Response({
            'date': now_date,
            'count': count
        })


class UserMonthCountView(APIView):
    """
        月增用户统计
    """
    # 权限指定
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 1. 获取当天时间
        now_date = date.today()
        # 2. 获取一个月之前的日期
        begin_date = now_date - timedelta(days=29)
        data_list = []
        for i in range(30):
            # 起始日期
            index_date = begin_date + timedelta(days=i)
            # 起始日期的下一天日期
            next_date = begin_date + timedelta(days=i + 1)
            count = User.objects.filter(date_joined__gte=index_date, date_joined__lt=next_date).count()
            data_list.append({
                'date': index_date,
                'count': count
            })
        # 3. 返回结果
        return Response(data_list)


class GoodsCountView(APIView):
    """
        日分类商品访问量
    """
    # 权限指定
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 1. 获取当天时间
        now_date = date.today()
        # 2. 获取当天注册用户总量
        goods = GoodsVisitCount.objects.filter(date__gte=now_date)
        ser = GoodsCountSerializer(goods, many=True)
        # 3. 返回结果
        return Response(ser.data)
