from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'cms'

router = DefaultRouter(trailing_slash=False)
router.register('merchant',views.MerchantViewSet,basename='merchant')
router.register('category',views.CategoryViewSet,basename='category')
router.register('goods',views.GoodsViewSet,basename='goods')
# /cms/merchant

urlpatterns = [
    path('login',views.LoginView.as_view(),name="login"),
    path('upload',views.PictureUploadView.as_view(),name='upload')
] + router.urls