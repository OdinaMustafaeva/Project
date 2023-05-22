from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    position = models.PositiveSmallIntegerField(default=1)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children", null=True, blank=True)

    def __str__(self):
        return self.title
