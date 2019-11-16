from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse

from webapp.forms import ProductForm
from webapp.models import Product, Review
from django.views.generic import ListView, DeleteView,DetailView,CreateView,UpdateView


class IndexView(ListView):
    template_name = 'webapp/product/index.html'
    context_object_name = 'products'
    model = Product

class ProductView(DetailView):
    template_name = 'webapp/product/product.html'
    model = Product
    context_object_name = 'product'


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = self.object
        reviews = Review.objects.all().filter(product=product)
        context['reviews'] = reviews
        return context


class ProductCreateView(PermissionRequiredMixin,CreateView):
    template_name = 'webapp/product/create.html'
    model = Product
    form_class = ProductForm
    permission_required = 'webapp.add_product'
    permission_denied_message = "Доступ запрещён"


    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin,UpdateView):
    form_class = ProductForm
    template_name = 'webapp/product/update.html'
    model = Product
    context_object_name = 'product'
    permission_required = 'webapp.change_product'
    permission_denied_message = "Доступ запрещён"

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

class ProductDeleteView(PermissionRequiredMixin,DeleteView):
    model = Product
    template_name = 'webapp/product/delete.html'
    success_url = reverse_lazy('webapp:index')
    context_object_name =  'product'
    permission_required = 'webapp.delete_product'
    permission_denied_message = "Доступ запрещён"