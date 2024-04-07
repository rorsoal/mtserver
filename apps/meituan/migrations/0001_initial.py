# Generated by Django 2.2 on 2024-03-27 07:48

import apps.meituan.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='商品名称')),
                ('picture', models.CharField(max_length=200, verbose_name='商品图片')),
                ('intro', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='商品价格')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名称')),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='商家名称')),
                ('address', models.CharField(max_length=200, verbose_name='商家')),
                ('logo', models.CharField(max_length=200, verbose_name='商家logo')),
                ('notice', models.CharField(blank=True, max_length=200, null=True, verbose_name='商家的公告')),
                ('up_send', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='起送价')),
                ('lon', models.FloatField(verbose_name='经度')),
                ('lat', models.FloatField(verbose_name='纬度')),
                ('create_time', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(default=apps.meituan.models.generate_order_uid, max_length=100, primary_key=True, serialize=False, verbose_name='订单id')),
                ('pay_method', models.SmallIntegerField(choices=[(0, '未选择'), (1, '微信支付'), (2, '支付宝')], default=0, verbose_name='支付方式')),
                ('order_status', models.SmallIntegerField(choices=[(1, '待支付'), (2, '待发货'), (3, '配送中'), (4, '待评价'), (5, '已完成')], default=1, verbose_name='订单状态')),
                ('goods_count', models.SmallIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='成交总价')),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realname', models.CharField(max_length=100, verbose_name='真是姓名')),
                ('telephone', models.CharField(max_length=11, verbose_name='手机号码')),
                ('province', models.CharField(max_length=100, verbose_name='省份')),
                ('city', models.CharField(max_length=100, verbose_name='城市')),
                ('county', models.CharField(max_length=100, verbose_name='区县')),
                ('address_detail', models.CharField(max_length=100, verbose_name='详细地址')),
                ('area_code', models.CharField(max_length=10, null=True, verbose_name='区域代号')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否是默认地址')),
            ],
        ),
    ]
