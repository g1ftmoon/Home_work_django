from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True)

    def __str__(self):
        return f"{self.name} --> {self.slug}"


class Product(models.Model):
    descr = models.TextField(max_length=100)
    price = models.PositiveIntegerField(default=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return f"{self.descr} >>> {self.price}"