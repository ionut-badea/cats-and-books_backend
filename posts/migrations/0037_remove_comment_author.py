# Generated by Django 3.0.3 on 2020-03-11 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0036_auto_20200311_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]