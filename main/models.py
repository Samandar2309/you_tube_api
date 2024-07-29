from django.db import models
from authentication.models import CustomUser


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Video(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    video = models.FileField(upload_to='videos/')
    like_count = models.IntegerField(default=0)
    watch_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
