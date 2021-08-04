"""  View for the Blog Categories  """

from django.contrib.auth import get_user_model

# Django REST Framework
from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from root.blog.api.permissions import IsBlogAdmin, IsVerified

from root.blog.api import serializers

# Models
from root.blog.models import Category, Post

# Serializers
from root.blog.api.serializers import PostModelSerializer, PostSerializer


class PostViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):

    serializer_class = PostModelSerializer
    lookup_field = "url"

    def get_permissions(self):
        """Assign permissions to posts based on actions."""

        if self.action in ["list", "retrieve"]:
            permissions = [AllowAny]
        elif self.action in [
            "create",
            "update",
            "partial_update",
        ]:
            permissions = [IsAuthenticated, IsVerified]
        elif self.action in ["destroy"]:
            permissions = [IsAuthenticated, IsBlogAdmin]
        return [permission() for permission in permissions]

    def get_queryset(self):
        """List all posts."""
        queryset = Post.published.all()
        return queryset

    def create(self, request, *args, **kwargs):
        """Handle the creation of posts"""

        serializer = PostSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        data = PostModelSerializer(post).data
        return Response(data, status=status.HTTP_201_CREATED)
        # return Response(data)
