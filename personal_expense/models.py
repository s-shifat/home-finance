from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    item_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['item_name']

    def __str__(self):
        return self.item_name


class Expense(models.Model):
    item_name = models.CharField(max_length=50)
    cost = models.DecimalField(decimal_places=2, max_digits=8,
            validators=[
                MinValueValidator(1, message="Spend at least 1 taka or higher! Not 0 or negative."),
            ]
        )
    date = models.DateTimeField(auto_now_add=True)
    paid_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
