"""  Serializer for the Blog Categories  """

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Model
from root.blog.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Category model serializer."""

    name = serializers.CharField(
        max_length=100,
        validators=[
            UniqueValidator(
                queryset=Category.objects.all(),
                message="The category name must be unique ⚠️",
            )
        ],
    )

    class Meta:
        """Meta class."""

        model = Category
        fields = ["name", "description"]
        read_only_fields = [
            "id",
        ]
