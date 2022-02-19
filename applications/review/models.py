from django.db import models
from applications.product.models import Product


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    text = models.TextField(max_length=50)
    # rating = models.IntegerField(default=5)
    rating = models.IntegerField(help_text='from 1 to 5')

    def __str__(self):
        return f"{self.product} --> {self.rating}"
