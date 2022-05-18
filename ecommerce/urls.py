from django.urls import path

from .views import *

urlpatterns = [
    path('',TypeCreateProduct.as_view(),name='home'),
    path('search',TypeCreateProduct.as_view(),name='search'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('edit/<int:pk>',ProductEditView.as_view(),name='product_edit'),
    path('delete/<int:pk>',ProductDeleteViewBlog.as_view(),name='product_delete'),
    path('add/',ProductAddView.as_view(),name='product_add'),
]