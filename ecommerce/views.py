from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *


# Create your views here.

class ProductListView(TemplateView):

    model = Type
    template_name = 'home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):

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

        context = {'product_list': q}
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    success_url = '/'


class ProductAddView(CreateView):
    model = Product
    template_name = 'product_add.html'
    fields = '__all__'
    context_object_name = 'form'
    success_url = '/'


class ProductEditView(UpdateView):
    model = Product
    template_name = 'product_edit.html'
    fields = '__all__'
    success_url = '/'
    context_object_name = 'form'


class ProductDeleteViewBlog(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    # success_url = '/'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse('detail', kwargs={'slug': self.object.slug})



class ContactUsView(CreateView):
    model = ContactUs
    template_name = 'contact.html'
    success_url = '/'
    fields = '__all__'

