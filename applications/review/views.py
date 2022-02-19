from rest_framework import generics

from applications.review.models import Review
from applications.review.serializer import ReviewSerializer


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer