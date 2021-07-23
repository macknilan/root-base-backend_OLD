""" Categories permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsCategoryAdmin(BasePermission):
    """Allow access only to categories admins for modify"""

    # https://www.django-rest-framework.org/api-guide/permissions/#examples
    def has_permission(self, request, view):
        """Verify user is a superuser and active"""

        if (
            request.user.is_authenticated
            and request.user.is_staff
            and request.user.is_superuser
        ):
            return True
        return False
