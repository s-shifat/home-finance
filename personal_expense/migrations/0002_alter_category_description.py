# Generated by Django 4.1.5 on 2023-02-13 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_expense', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
