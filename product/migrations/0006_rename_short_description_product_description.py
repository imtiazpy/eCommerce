# Generated by Django 3.2.12 on 2022-03-22 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_is_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='short_description',
            new_name='description',
        ),
    ]
