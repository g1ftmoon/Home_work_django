from rest_framework import serializers

from applications.review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'rating')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('id')
        representation['review'] = ReviewSerializer(Review.objects.get(review=instance.id)).data

        return