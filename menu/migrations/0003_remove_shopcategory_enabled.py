# Generated by Django 3.1.5 on 2021-01-18 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_shopcategory_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcategory',
            name='enabled',
        ),
    ]
