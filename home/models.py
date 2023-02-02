from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from datetime import datetime
from django.core.exceptions import ValidationError

# TODO:
# - add choice list in Bill.name
# - add update method on bill transaction
# - Home Rent, Electricity, Dish, Internet, Gas, Home Maid, Garbage

# Create your models here.
class Bill(models.Model):
    name = models.CharField(max_length=40, blank=False)
    amount = models.DecimalField(default=0, max_digits=8, decimal_places=2, blank=False)
    paid_amount = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    payers = models.CharField(max_length=200, default='', blank=True)
    due_date = models.DateField(blank=False)
    status = models.BooleanField(default=False)
    clearance_date = models.DateField(blank=True, null=True)
    def __str__(self):
        # datetime.datetime.strftime(today, '%B') 
        month = datetime.strftime(self.due_date, "%B")
        year = self.due_date.year
        return f"{self.name} - {month} - {year} = {self.id}"


class BillTransaction(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    paid_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid_amount = models.DecimalField(
            default=0,
            max_digits=8,
            decimal_places=2,
            validators=[
                MinValueValidator(1, message="Pay at least 1 taka or higher! Not 0 or negative."),
            ]
    )
    date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        #self.bill.paid_amount += self.paid_amount
        if self.bill.paid_amount - self.bill.amount == 0:
            self.bill.status = True
        elif self.bill.paid_amount < self.bill.amount:
            self.bill.status = False
        self.bill.save()
        return super(BillTransaction, self).save(*args, **kwargs)

    def __str__(self):
        # datetime.datetime.strftime(today, '%B') 
        month = datetime.strftime(self.bill.due_date, "%B")
        year = self.bill.due_date.year
        return f"{self.bill.name} - {month} - {year} by {self.paid_by}"

