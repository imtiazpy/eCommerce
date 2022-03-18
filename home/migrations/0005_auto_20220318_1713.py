# Generated by Django 3.2.12 on 2022-03-18 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('home', '0004_homepage_header_carousel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcustomfield',
            name='product',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductCustomField',
        ),
    ]
