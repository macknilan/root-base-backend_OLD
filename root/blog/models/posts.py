""" Model Post for the Blog """

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

# Utilities
from root.utils.models import RootBaseModel

# Models
from root.blog.models import Category

# https://docs.djangoproject.com/en/3.2/topics/db/managers/#modifying-a-manager-s-initial-queryset
class PostLet(models.Manager):
    def get_queryset(self):
        """Show posts less than or equal to (lte) now"""
        now = timezone.now()
        return super().get_queryset().filter(publish_date__lte=now)


class Post(RootBaseModel):
    """Post model."""

    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    categories = models.ForeignKey(Category, on_delete=models.RESTRICT, null=True)
    title = models.CharField(_("title"), max_length=255)
    intro = models.CharField(_("intro"), max_length=255)
    body = models.TextField()
    image_header = models.ImageField(_("image_header"), upload_to="posts/photos", blank=True, null=True)
    is_draft = models.BooleanField(_("is_draft"), default=True)
    url = models.SlugField(_("url"), max_length=255, unique=True)
    publish_date = models.DateTimeField(_("published_date"), auto_now=False, auto_now_add=False, null=True, blank=True)

    objects = models.Manager()  # The default manager
    published = PostLet()  # The Post Manager manager

    class Meta(RootBaseModel.Meta):
        """Overwrite meta class of RootBaseModel"""

        # ordering = ("title",)
        ordering = [
            "-publish_date",
        ]

    def __str__(self):
        """Return title and username."""
        return "{} by @{}".format(self.title, self.user.username)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
