# Generated by Django 3.2.12 on 2022-03-24 12:18

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20220324_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available_colors',
            field=models.CharField(blank=True, help_text='Add available colors with coma. ie:Red,Green,Blue', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='available_sizes',
            field=models.CharField(blank=True, help_text='Add available sizes with coma. ie: S,M,L', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_images',
            field=wagtail.core.fields.StreamField([('images', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))], blank=True, null=True),
        ),
    ]