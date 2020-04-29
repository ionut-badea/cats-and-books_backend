# Generated by Django 3.0.4 on 2020-04-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0050_comment_reviewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='articles', to='posts.Tag'),
        ),
    ]