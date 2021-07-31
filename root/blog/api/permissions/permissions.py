""" Categories permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsBlogAdmin(BasePermission):
    """Allow access only to categories admins for modify"""

    # https://www.django-rest-framework.org/api-guide/permissions/#examples
    def has_permission(self, request, view):
        """Allow access only if verified, staff and superuser"""

        if (
            request.user.is_verified
            and request.user.is_staff
            and request.user.is_superuser
        ):
            return True
        return False


class IsVerified(BasePermission):
    """Allow access only to categories admins for modify"""

    # https://www.django-rest-framework.org/api-guide/permissions/#examples
    def has_permission(self, request, view):
        """Allow access only if verified"""

        if request.user.is_verified:
            return True
        return False
