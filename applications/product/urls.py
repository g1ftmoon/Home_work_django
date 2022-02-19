from django.urls import path

from applications.product.views import ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view()),
]