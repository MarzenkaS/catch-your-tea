# Generated by Django 3.2.25 on 2024-06-18 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttestimonial',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
