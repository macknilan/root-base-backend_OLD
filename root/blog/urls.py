""" Blog / Templates URL's """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from root.blog.api.views import CategoryViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"categories", CategoryViewSet, basename="categories")
app_name = "blog"

urlpatterns = [
    # API
    path("", include(router.urls)),
]
