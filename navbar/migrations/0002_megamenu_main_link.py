# Generated by Django 3.2.12 on 2022-03-30 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='megamenu',
            name='main_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Main Navigation Link'),
        ),
    ]
