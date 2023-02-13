from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class TodoList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.list_name

class TodoItem(models.Model):
    item_name = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now_add=True)
    clearance_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
