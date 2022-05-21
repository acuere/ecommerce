import imp
from django.urls import path
from .views import *

urlpatterns = [
    path('products/',ProductViewSet.as_view({'get':'list'}),name='products'),
    path('contact/',ContactUsViewSet.as_view({'get':'list'}),name='contact'),
    path('type/',TypeViewSet.as_view({'get':'list'}),name='type'),

]