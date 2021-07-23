"""  Serializer for the Blog Categories  """

# Django REST Framework
from rest_framework import serializers

# Model
from root.blog.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Category model serializer."""

    # name = serializers.CharField(required=True)

    class Meta:
        """Meta class."""

        model = Category
        fields = ("name",)
