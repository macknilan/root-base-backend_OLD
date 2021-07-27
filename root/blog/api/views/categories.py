"""  View for the Blog Categories  """

from django.contrib.auth import get_user_model

# Django REST Framework
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from root.blog.api import serializers

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
    mixins.DestroyModelMixin,
    GenericViewSet,
):

    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]
    # queryset = Category.objects.all()
    lookup_field = "name"

    def get_permissions(self):
        """Assign permissions to categories based on actions."""

        if self.action in ["list"]:
            permissions = [AllowAny]
        elif self.action in [
            "create",
            "retrieve",
            "update",
            "partial_update",
            "destroy",
        ]:
            permissions = [IsCategoryAdmin]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]

    def get_queryset(self):
        """List all categories."""
        queryset = Category.objects.all()
        return queryset

    # def create(self, request, *args, **kwargs):
    #     serializer = CategorySerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
