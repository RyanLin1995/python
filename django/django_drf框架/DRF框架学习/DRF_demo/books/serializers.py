from .models import BookInfo
from rest_framework import serializers


# 定义一个用于嵌套的序列化器
class HeroinfoSerializer(serializers.Serializer):
    """
        一个英雄信息的序列化器
    """
    name = serializers.CharField()
    skill = serializers.CharField()

    hbook = serializers.StringRelatedField()  # 多对一，不用 many


# 自定义序列化器
class BookSerializer(serializers.Serializer):
    """
        一个图书数据的序列化器
        要使用序列化器，需要先自定义一个序列化器，然后在视图中将数据传递到这个序列化器中
    """
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    btitle = serializers.CharField(max_length=20, min_length=5)  # 添加字段验证
    bread = serializers.IntegerField()
    # bread = serializers.IntegerField(read_only=True)  # read_only 表示该字段只参与序列化返回，不参与验证；
    # write_only 表示该字段只参与序列化过程，不参与反序列化过程
    bpub_date = serializers.DateField(required=False)  # required=False 设定该字段不是必须传递的
    bcomment = serializers.IntegerField(default=10)

    # 嵌套序列化返回的使用
    # 1. 返回关联的英雄ID
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # 2. 返回关联英雄模型类的str方法值
    # heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)
    # 3. 嵌套序列化器
    # heroinfo_set = HeroinfoSerializer(many=True)

    # 自定义验证方法
    # 单一字段验证
    def validate_btitle(self, value):  # value 参数名称可以为任意

        if value == 'python':
            raise serializers.ValidationError('书名不能为 python')

        return value

    # 多个字段验证
    def validate(self, attrs):  # attrs 参数名称可以为任意

        if attrs['bread'] > attrs['bcomment']:
            raise serializers.ValidationError('阅读量大于评论量')

        return attrs

    # 保存数据
    def create(self, validated_data):

        book = BookInfo.objects.create(**validated_data)
        return book

    # 更新数据
    def update(self, instance, validated_data):

        instance.btitle = validated_data['btitle']
        instance.bread = validated_data['bread']
        instance.save()
        return instance


# 定义模型序列化器
class BookModelSerializer(serializers.ModelSerializer):
    # 添加/修改字段选项参数方法一：显式指明修改字段
    bread = serializers.IntegerField(max_value=100, min_value=20)
    # 显式指明可以指明模型没有的字段
    sms_code = serializers.CharField(max_length=6, min_length=6)

    class Meta:
        model = BookInfo  # 指定生成字段的模型类
        # fields = ('btitle', 'bread')  # 指定模型类中的字段
        fields = '__all__'  # 指定模型类中的所有字段，如果显式指明模型类没有的字段，fields 必须为 '__all__'
        # exclude = ('btitle')  # 排除不需要的字段

        # 添加 read only 字段
        read_only_fields = ('btitle',)

        # 添加 write only 字段
        write_only_fields = ('bread',)

        # 添加/修改字段选项参数方法二：extra_kwargs
        extra_kwargs = {
            "bcomment": {
                "max_value": 100
            },
            "btitle": {
                "min_length": 5
            }
        }
