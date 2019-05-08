from django.conf import settings
from django.db import models
# Create your models here.
User = settings.AUTH_USER_MODEL


class Todo(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    text = models.TextField(verbose_name = "Text")
    is_completed = models.BooleanField(verbose_name = "Status")
    created_time = models.DateTimeField(auto_now_add=True) 
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id', '-created_time']

    def __str__(self):
        return self.text