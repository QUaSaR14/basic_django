from datetime import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=124)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
