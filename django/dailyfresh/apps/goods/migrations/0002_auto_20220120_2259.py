# Generated by Django 3.2.5 on 2022-01-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='删除标记'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='image',
            field=models.ImageField(upload_to='goods', verbose_name='图片路径'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='删除标记'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='image',
            field=models.ImageField(upload_to='goods', verbose_name='商品图片'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='删除标记'),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='image',
            field=models.ImageField(upload_to='type', verbose_name='商品类型图片'),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='删除标记'),
        ),
        migrations.AlterField(
            model_name='indexgoodsbanner',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='删除标记'),
        ),
        migrations.AlterField(
            model_name='indexpromotionbanner',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='删除标记'),
        ),
        migrations.AlterField(
            model_name='indextypegoodsbanner',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='删除标记'),
        ),
    ]