# Generated by Django 3.1.3 on 2020-12-22 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Article', '0002_auto_20201222_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog',
            new_name='article',
        ),
    ]
