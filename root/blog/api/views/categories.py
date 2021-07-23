"""  View for the Blog Categories  """

from django.contrib.auth import get_user_model

# Django REST Framework
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

# Permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from root.blog.api.permissions import IsCategoryAdmin

# Models
from root.blog.models import Category

# Serializers
from root.blog.api.serializers import CategorySerializer


class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "name"

    def get_permissions(self):
        """Assign permissions based on action"""

        if self.action in ["list"]:
            permissions = [IsAuthenticated]
        elif self.action in ["create", "update", "partial_update"]:
            permissions = [IsAuthenticated, IsCategoryAdmin]
        return [permission() for permission in permissions]
