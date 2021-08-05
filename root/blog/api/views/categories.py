"""  View for the Blog Categories  """

from django.contrib.auth import get_user_model
from django.db.models import RestrictedError

# Django REST Framework
from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from root.blog.api import serializers
from root.blog.api.permissions import IsBlogAdmin

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
    lookup_field = "name"

    def get_permissions(self):
        """Assign permissions to categories based on actions."""

        if self.action in ["list", "retrieve"]:
            permissions = [AllowAny]
        elif self.action in [
            "create",
            "update",
            "partial_update",
            "destroy",
        ]:
            permissions = [IsBlogAdmin]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]

    def get_queryset(self):
        """List all categories."""
        queryset = Category.objects.all()
        return queryset

    def destroy(self, request, *args, **kwargs):
        """Verify that when a category is deleted it is not related to any post."""

        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except RestrictedError:
            data = {
                "message": "Can not delete: this  category has posts! (parent has a child) ة_ة"
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_204_NO_CONTENT)
