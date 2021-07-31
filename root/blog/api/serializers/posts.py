"""  Serializer for the Blog Categories  """

# Django REST Framework
from django.db.models import fields
from rest_framework import serializers

# from rest_framework.validators import UniqueValidator

# Model
from root.blog.models import Post, Category


class PostModelSerializer(serializers.ModelSerializer):
    """Post model serializer"""

    class Meta:
        """Meta class"""

        model = Post
        fields = (
            "user",
            "categories",
            "title",
            "intro",
            "body",
            "image_header",
            "is_draft",
            "url",
            "publish_date",
        )


class PostSerializer(serializers.ModelSerializer):
    """Handle the post model serializer."""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    categories = serializers.CharField(min_length=10, max_length=100)
    title = serializers.CharField(min_length=20, max_length=255)
    intro = serializers.CharField(min_length=20, max_length=255)
    body = serializers.CharField(min_length=20, max_length=1000)
    is_draft = serializers.BooleanField(default=False)
    publish_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    image_header = serializers.ImageField(
        max_length=20, allow_null=True, required=False
    )
    # url = serializers.CharField(min_length=10, max_length=255, required=False)

    class Meta:
        """Meta class."""

        model = Post
        fields = [
            "user",
            "categories",
            "title",
            "intro",
            "body",
            "is_draft",
            "publish_date",
            "image_header",
        ]
        read_only_fields = [
            "id",
        ]

    def validate_categories(self, data):
        """Validate that the category to be assigned exists"""

        try:
            cat = Category.objects.get(name=data)
            # print(f"self.context[categories] ---> {self.context['categories']}")
        except Category.DoesNotExist:
            raise serializers.ValidationError(
                "The category does not exist with that name."
            )
        return data

    def validate_title(self, data):
        """Validate that the title not be repeated"""

        q = Post.objects.filter(title=data)
        if q.exists():
            raise serializers.ValidationError("The title it's repeated.")
        return data

    def create(self, data):
        """Create new post."""

        # Create post
        post = Post.objects.create(
            user=data["user"],
            categories=Category.objects.get(name=data["categories"]),
            title=data["title"],
            intro=data["intro"],
            body=data["body"],
            image_header=data["image_header"],
            is_draft=data["is_draft"],
            publish_date=data["publish_date"],
        )
        return post

    def update(self, instance, data):
        """Update post."""

        # Post.objects.get(title=self.data['title'])
        # self.context['request'].data['title']
        # import ipdb; ipdb.set_trace()
        # breakpoint()

        instance.title = data.get("title", instance.title)
        instance.intro = data.get("intro", instance.intro)
        instance.body = data.get("body", instance.body)
        instance.image_header = data.get("image_header", instance.image_header)
        instance.is_draft = data.get("is_draft", instance.is_draft)
        instance.publish_date = data.get("publish_date", instance.publish_date)
        instance.categories = Category.objects.get(name=data["categories"])
        instance.save()

        return instance
