from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS = (
        ('draft','Draft'),
        ('publish', 'Publish'),
    )
    status = models.CharField(max_length=10, choices=STATUS, default=STATUS[0][0])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    