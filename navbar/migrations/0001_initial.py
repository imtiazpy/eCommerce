# Generated by Django 3.2.12 on 2022-03-15 23:02

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavTopLevelItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Navigation Name')),
                ('main_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Main Navigation Link')),
                ('position', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Top Level Item',
            },
        ),
        migrations.CreateModel(
            name='OrderableMenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_title', models.CharField(blank=True, max_length=50, null=True)),
                ('link_url', models.CharField(blank=True, max_length=500)),
                ('open_in_new_tab', models.BooleanField(blank=True, default=False)),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MegaMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('navigation', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='mega_menu', to='navbar.navtoplevelitem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MegaMenuItem',
            fields=[
                ('orderablemenuitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='navbar.orderablemenuitem')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='mega_menu_items', to='navbar.megamenu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('navbar.orderablemenuitem',),
        ),
    ]
