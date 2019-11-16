from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import  ReviewForm
from webapp.models import  Review
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


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:status_view', kwargs={'pk': self.object.pk})


class ReviewUpdateView(UpdateView):
    form_class = ReviewForm
    template_name = 'webapp/review/update.html'
    model = Review
    context_object_name = 'review'



    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:status_view', kwargs={'pk': self.object.pk})

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'webapp/review/delete.html'
    success_url = reverse_lazy('webapp:status')
    context_object_name =  'review'


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)
