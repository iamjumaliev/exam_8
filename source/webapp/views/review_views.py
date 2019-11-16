from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from webapp.forms import  ReviewForm
from webapp.models import Review, Product
from django.views.generic import ListView, CreateView,DeleteView,UpdateView,DetailView



class ReviewIndexView(ListView):
    template_name = 'webapp/review/index.html'
    context_object_name = 'reviews'
    model = Review


class ReviewView(DetailView):

    template_name = 'webapp/review/review.html'
    model = Review
    context_object_name = 'review'


class ReviewCreateView(CreateView):
    template_name = 'webapp/review/create.html'
    model = Review
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, pk=self.kwargs['pk'])
        return context

    def get_form(self, form_class=None):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        form = super().get_form(form_class=None)
        form.instance.author = self.request.user
        form.instance.product = product
        return form


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:reviews_view', kwargs={'pk': self.object.pk})


class ReviewUpdateView(PermissionRequiredMixin,UpdateView):
    form_class = ReviewForm
    template_name = 'webapp/review/update.html'
    model = Review
    context_object_name = 'review'
    permission_required = 'webapp.change_review'
    permission_denied_message = "Доступ запрещён"

    def has_permission(self):
        super().has_permission()
        return super().has_permission() or self.request.user == self.get_object().author

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:reviews_view', kwargs={'pk': self.object.pk})

class ReviewDeleteView(PermissionRequiredMixin,DeleteView):
    model = Review
    template_name = 'webapp/review/delete.html'
    success_url = reverse_lazy('webapp:review_index')
    context_object_name =  'review'
    permission_required = 'webapp.delete_review'
    permission_denied_message = "Доступ запрещён"

    def has_permission(self):
        super().has_permission()
        return super().has_permission() or self.request.user == self.get_object().author

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)
