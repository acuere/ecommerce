
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('product/', CreateProductViewSet.as_view(), name='product'),
    path('products/', ProductViewSet.as_view({'get': 'list'}), name='products'),
    path('contact/', ContactUsViewSet.as_view({'get': 'list'}), name='contact'),
    path('type/', TypeViewSet.as_view({'get': 'list'}), name='type'),
]
