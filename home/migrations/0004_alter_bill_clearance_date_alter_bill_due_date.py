# Generated by Django 4.1.5 on 2023-01-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_bill_cleared_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='clearance_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
