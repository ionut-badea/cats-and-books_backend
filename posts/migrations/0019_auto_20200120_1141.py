# Generated by Django 2.2.7 on 2020-01-20 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
    ]