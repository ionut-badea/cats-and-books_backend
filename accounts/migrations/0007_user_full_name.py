# Generated by Django 3.0.4 on 2020-04-29 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200429_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='full name'),
        ),
    ]
