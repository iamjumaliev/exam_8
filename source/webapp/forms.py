from django import forms

from webapp.models import Product,Review
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','description','picture']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['author','product']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating > 5 or rating < 1:
            raise ValidationError('Error, rating should be between 1 and 5', code='wrong_rating')
        return rating