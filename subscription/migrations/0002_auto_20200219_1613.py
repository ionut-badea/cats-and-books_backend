# Generated by Django 3.0.3 on 2020-02-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='2020-02-19', verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
    ]