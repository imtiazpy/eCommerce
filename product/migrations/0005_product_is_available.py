# Generated by Django 3.2.12 on 2022-03-22 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20220322_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=False, verbose_name='Is Available'),
        ),
    ]
