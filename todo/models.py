from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_add_now=True)
    clearance_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

