# Generated by Django 3.1.3 on 2020-12-23 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Quiz', '0004_auto_20201223_1531'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='question',
            table='Question',
        ),
        migrations.AlterModelTable(
            name='quiz',
            table='Quiz',
        ),
    ]