from django.urls import path

from applications.review.views import ReviewListView

urlpatterns = [
    path('reviews/', ReviewListView.as_view()),
]