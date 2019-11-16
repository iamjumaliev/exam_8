from django.urls import path
from .views import IndexView, ProductCreateView, ProductView,  ProductDeleteView,ProductUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/delete/<int:pk>/',ProductDeleteView.as_view(),name = 'product_delete'),
    path('product/update/<int:pk>/',ProductUpdateView.as_view(),name = 'product_update')
]
