# Generated by Django 3.1.3 on 2020-12-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0004_auto_20201223_0230'),
        ('App_Quiz', '0011_auto_20201224_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='participiants',
            field=models.ManyToManyField(blank=True, to='App_Login.Student'),
        ),
    ]