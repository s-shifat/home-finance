# Generated by Django 4.1.5 on 2023-02-07 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_bill_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='payers',
        ),
    ]
