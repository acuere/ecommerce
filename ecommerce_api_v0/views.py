from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets
from ecommerce.models import *
from .serializer import *
from rest_framework import permissions
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        q = Product.objects.all()
        url_dict = self.request.GET

        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(name__icontains=text))

        if 'from-price' in url_dict and url_dict['from-price']:
            from_price = int(url_dict.get('from-price'))
            q = q.filter(price__gte=from_price)

        if 'to-price' in url_dict and url_dict['to-price']:
            from_price = int(url_dict.get('to-price'))
            q = q.filter(price__lte=from_price)

        if 'search-type' in url_dict and url_dict['search-type']:
            text = url_dict.get('search-type')
            q = q.filter(Q(type__name__icontains=text))

        return q

class TypeViewSet(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        q = Type.objects.all()
        url_dict = self.request.GET

        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(name__icontains=text))

        return q

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def get_queryset(self):
        q = ContactUs.objects.all()
        url_dict = self.request.GET

        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(name__icontains=text))

        if 'from-price' in url_dict and url_dict['from-price']:
            from_price = int(url_dict.get('from-price'))
            q = q.filter(price__gte=from_price)

        if 'to-price' in url_dict and url_dict['to-price']:
            from_price = int(url_dict.get('to-price'))
            q = q.filter(price__lte=from_price)

        if 'search-type' in url_dict and url_dict['search-type']:
            text = url_dict.get('search-type')
            q = q.filter(Q(type__name__icontains=text))

        return q