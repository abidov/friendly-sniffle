from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    """Posts Model"""

    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upvote_count = models.PositiveIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def count_increase(self) -> None:
        self.upvote_count += 1
        self.save()
        return None


class Comment(models.Model):
    """Comments Model"""

    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Comment by id of {self.id}"
