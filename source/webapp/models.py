from django.db import models
from django.contrib.auth.models import User
from django.db import models

CATEGORY_CHOICES = (
    ('other', 'Другое'),
    ('cars', 'Машины'),
    ('books', 'Книги'),
    ('music', 'Музыка'),
)


class Product(models.Model):

    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='название')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категория',null=False, blank=True)
    description = models.CharField(max_length=3000, null=False, blank=True, verbose_name='описание')
    picture =  models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='картинка')

    def get_rating(self):
        reviews = self.product_review.all()
        qty = len(reviews)
        rate = 0
        for product in reviews:
            rating = product.rating
            rate += rating
        if qty == 0:
            mark = rate / 1
        else:
            mark = rate / qty
        return mark

class Review(models.Model):
        author = models.ForeignKey(User,related_name='review_creator',on_delete=models.CASCADE,
                                   verbose_name='автор',null=False,blank=False)
        product = models.ForeignKey('webapp.Product',on_delete=models.CASCADE,verbose_name='продукт',null=False,
                                    blank=False,related_name='product_review')
        text = models.CharField(max_length=3000, null=False, blank=False, verbose_name='описание')
        rating = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='оценка',null=False, blank=False)

# Create your models here.
