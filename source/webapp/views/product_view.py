from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse

from webapp.forms import ProductForm
from webapp.models import Product
from django.views.generic import ListView, DeleteView,DetailView,CreateView,UpdateView


class IndexView(ListView):
    template_name = 'webapp/product/index.html'
    context_object_name = 'products'
    model = Product


class ProductView(DetailView):
    template_name = 'webapp/product/product.html'
    model = Product
    context_object_name = 'product'




class ProductCreateView(CreateView):
    template_name = 'webapp/product/create.html'
    model = Product
    form_class = ProductForm


    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    form_class = ProductForm
    template_name = 'webapp/product/update.html'
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'webapp/product/delete.html'
    success_url = reverse_lazy('webapp:index')
    context_object_name =  'product'