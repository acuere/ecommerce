from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, generics
from ecommerce.models import *
from .serializer import *
from rest_framework import permissions


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateProductViewSet(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        return super().post(request, *args, **kwargs)
