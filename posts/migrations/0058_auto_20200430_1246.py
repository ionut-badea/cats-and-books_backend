# Generated by Django 3.0.4 on 2020-04-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0057_auto_20200430_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.TextField(blank=True, max_length=303, verbose_name='abstract'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(blank=True, verbose_name='body'),
        ),
    ]
