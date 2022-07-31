from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Prayer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    prayer = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    answered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    priority = models.BooleanField(default=False)
#did not use created, updated, or priority, but I am leaving them incase I come back and play with these things in the future.

    def __str__(self):
        return self.prayer

    class Meta:
        ordering = ['answered', '-priority', '-updated', '-created']
