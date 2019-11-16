from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse

from webapp.forms import ProductForm
from webapp.models import Product
from django.views.generic import ListView, DeleteView,DetailView,CreateView,UpdateView


class IndexView(ListView):
    template_name = 'webapp/product/index.html'
    context_object_name = 'polls'
    model = Product
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class PollView(DetailView):
    template_name = 'webapp/product/product.html'
    model = Product
    context_object_name = 'poll'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = self.object
        choices = poll.choice_poll.all()
        self.paginate_choices_to_context(choices, context)
        return context

    def paginate_choices_to_context(self, choices, context):
        paginator = Paginator(choices, 5, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['choices'] = page.object_list
        context['is_paginated'] = page.has_other_pages()



class PollCreateView(CreateView):
    template_name = 'webapp/product/create.html'
    model = Product
    form_class = ProductForm


    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    form_class = ProductForm
    template_name = 'webapp/product/update.html'
    model = Product
    context_object_name = 'mission'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})

class PollDeleteView(DeleteView):
    model = Product
    template_name = 'webapp/product/delete.html'
    success_url = reverse_lazy('index')
    context_object_name =  'poll'