from rest_framework import generics

from applications.product.models import Product
from applications.product.serializer import ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer