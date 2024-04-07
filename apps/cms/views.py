from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.utils.timezone import now
from apps.mtauth.authentications import generate_jwt,JWTAuthentication
from apps.mtauth.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from apps.meituan.serializers import MerchantSerializer,GoodsCategorySerializer,GoodsSerializer
from apps.meituan.models import Merchant,GoodsCategory,Goods
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
import shortuuid
import os
from django.conf import settings
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework import status

class MerchantPagination(PageNumberPagination):
    page_size = 12
    page_query_param = "page"

class CmsBaseView(object):
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    pass

# class LoginView(APIView):
#     def post(self,request):
#         serializer = AuthTokenSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data.get('user')
#             user.last_login = now()
#             user.save()
#             token = generate_jwt(user)
#             user_serializer = UserSerializer(user)
#             return Response({"token":token,"user":user_serializer.data})
#         else:
#             return Response({"message":"用户名或密码错误！"})
class LoginView(APIView):
    def post(self, request):
        # 1. 创建 AuthTokenSerializer 实例，传入请求数据
        serializer = AuthTokenSerializer(data=request.data)
        print(serializer)

        # 2. 验证序列化器数据
        if serializer.is_valid():
            # 3. 如果数据有效，从 validated_data 获取已验证的用户对象
            user = serializer.validated_data.get('user')

            # 4. 更新用户最后登录时间
            user.last_login = now()
            user.save()

            # 5. 生成 JWT（JSON Web Token）
            token = generate_jwt(user)
            print(user)

            # 6. 使用 UserSerializer 序列化用户对象
            user_serializer = UserSerializer(user)

            # 7. 返回包含 token 和用户数据的响应
            return Response({"token": token, "user": user_serializer.data})

        # 8. 如果数据无效（用户名或密码错误），返回错误消息
        else:
            return Response({"message": "用户名或密码错误！","status":400})
class MerchantViewSet(CmsBaseView,viewsets.ModelViewSet):
    queryset = Merchant.objects.order_by("-create_time").all()
    serializer_class = MerchantSerializer
    pagination_class = MerchantPagination

# Create,Update,Destroy,Retrieve
class CategoryViewSet(
    CmsBaseView,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategorySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.goods_list.count() > 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

    # /cms/category/merchant/<int:merchant_id>
    @action(['GET'],detail=False,url_path="merchant/(?P<merchant_id>\d+)")
    def merchant_category(self,request,merchant_id=None):
        queryset = self.get_queryset()
        seriazlier_class = self.get_serializer_class()
        categories = queryset.filter(merchant=merchant_id)
        serializer = seriazlier_class(categories,many=True)
        return Response(serializer.data)

class GoodsViewSet(
    CmsBaseView,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

class PictureUploadView(CmsBaseView,APIView):
    def save_file(self,file):
        # 肯德基.jpg = ('肯德基,'.jpg')
        filename = shortuuid.uuid() + os.path.splitext(file.name)[-1]
        filepath = os.path.join(settings.MEDIA_ROOT,filename)
        with open(filepath,'wb') as fp:
            for chunk in file.chunks():
                fp.write(chunk)
        # http://127.0.0.1:8000/media/abc.jpg
        return self.request.build_absolute_uri(settings.MEDIA_URL + filename)

    def post(self,request):
        file = request.data.get('file')
        file_url = self.save_file(file)
        return Response({"picture":file_url})














