# Generated by Django 3.2.25 on 2024-07-08 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_amount_in_gram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount_in_gram',
            field=models.IntegerField(blank=True, default=50, null=True),
        ),
    ]