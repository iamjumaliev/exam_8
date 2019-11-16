from django.urls import path

from webapp.views import ReviewIndexView, ReviewUpdateView, ReviewDeleteView, ReviewCreateView, ReviewView
from .views import IndexView, ProductCreateView, ProductView,  ProductDeleteView,ProductUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/delete/<int:pk>/',ProductDeleteView.as_view(),name = 'product_delete'),
    path('product/update/<int:pk>/',ProductUpdateView.as_view(),name = 'product_update'),
    path('reviews/', ReviewIndexView.as_view(), name='review_index'),
    path('reviews/<int:pk>/', ReviewView.as_view(), name='reviews_view'),
    path('product/<int:pk>review/create/', ReviewCreateView.as_view(), name='reviews_create'),
    path('reviews/delete/<int:pk>/',ReviewDeleteView.as_view(),name = 'reviews_delete'),
    path('reviews/update/<int:pk>/',ReviewUpdateView.as_view(),name = 'reviews_update')
]
