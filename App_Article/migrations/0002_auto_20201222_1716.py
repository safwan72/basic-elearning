# Generated by Django 3.1.3 on 2020-12-22 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-publish_date',), 'verbose_name_plural': 'Article'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Comment'},
        ),
        migrations.AlterModelTable(
            name='article',
            table='Article',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='Comment',
        ),
    ]
