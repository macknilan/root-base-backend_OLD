""" Blog / Templates URL's """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from root.blog.api.views import CategoryViewSet, PostViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"post", PostViewSet, basename="post")
app_name = "blog"

urlpatterns = [
    # API
    path("", include(router.urls)),
]
