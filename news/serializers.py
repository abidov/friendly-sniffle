from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
)

from .models import Post, Comment


class PostSerializer(ModelSerializer):
    link = HyperlinkedIdentityField(view_name="post-detail", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id", "title", "link", "creation_date", "upvote_count", "author"
        ]

    def to_representation(self, instance):
        rep = super(PostSerializer, self).to_representation(instance)
        rep["author"] = instance.author.username
        return rep


class PostCreateOrUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "creation_date", "author"]

    def to_representation(self, instance):
        rep = super(CommentSerializer, self).to_representation(instance)
        rep["author"] = instance.author.username
        return rep


class CommentCreateOrUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content"]
