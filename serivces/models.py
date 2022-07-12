from django.db import models
from django.contrib.auth.models import User


class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_url = models.URLField()
    alias = models.CharField(max_length=8, unique=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-timestamp', )

