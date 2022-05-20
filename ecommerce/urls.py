from django.urls import path

from .views import *

urlpatterns = [
    path('',ProductListView.as_view(),name='home'),
    path('search',ProductListView.as_view(),name='search'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('edit/<int:pk>',ProductEditView.as_view(),name='product_edit'),
    path('delete/<int:pk>',ProductDeleteViewBlog.as_view(),name='product_delete'),
    path('add/',ProductAddView.as_view(),name='product_add'),
    path('contact/',ContactUsView.as_view(),name='contact'),
    path('texnika/',CategoryView.as_view(),name='texnika'),
]
