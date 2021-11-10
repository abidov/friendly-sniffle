from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post
from .serializers import (
    PostSerializer,
    PostCreateOrUpdateSerializer,
    CommentSerializer,
    CommentCreateOrUpdateSerializer,
)
from .mixins import GetSerializerClassMixin
from .permissions import IsOwnerOrReadOnly


class PostViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    serializer_action_classes = {
        "create": PostCreateOrUpdateSerializer,
        "update": PostCreateOrUpdateSerializer,
    }

    @action(detail=True, methods=["post"])
    def upvote(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        post.count_increase()
        return Response({"message": "upvoted"})

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    serializer_action_classes = {
        "create": CommentCreateOrUpdateSerializer,
        "update": CommentCreateOrUpdateSerializer,
    }

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        return post.comment_set.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        serializer.save(author=self.request.user, post=post)
