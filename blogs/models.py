import random

from django.db import models
from django.utils.text import slugify


# Create your models here.

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(TimestampModel):
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(null=True, upload_to="blogs")
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE, related_name="categories")
    collab = models.ManyToManyField(
        "users.User", related_name='collab', blank=True)
    body = models.TextField()

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        slug = self.slug
        while self.__class__.objects.filter(slug=slug).exists():
            slug = f"{self.slug}-{random.randint(1, 100000)}"
        self.slug = slug
        return super().save(*args, **kwargs)


class LikeDislike(TimestampModel):
    class LikeType(models.TextChoices):
        dislike = "-"
        like = "+"

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="LikeDislikeBlog")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="LikeDislikeUser")
    type = models.CharField(max_length=20, choices=LikeType.choices)

    def __str__(self):
        return f"{self.user}"


class Comments(TimestampModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="CommentsBlog")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="CommentsUser")
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.body[0:50]
