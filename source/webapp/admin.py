from django.contrib import admin
from django.contrib import admin
from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product')
    list_filter = ('rating',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Review,ReviewAdmin)
# Register your models here.
