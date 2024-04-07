from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('merchant',views.MerchantViewSet,basename="merchant")
router.register('address',views.AddressViewSet,basename='address')

app_name = "smscode"
urlpatterns = [
    path("smscode",views.SMSCodeView.as_view(),name="smscode"),
    path("login",views.LoginView.as_view(),name="login"),
    path("search",views.MerchantSearchView.as_view(),name="search"),
    path('category/merchant/<int:merchant_id>',views.CategoryView.as_view(),name="category"),
    path('submitorder',views.CreateOrderView.as_view(),name='submitorder'),
    path('callback',views.AlipayCallbackView.as_view(),name="callback")
] + router.urls