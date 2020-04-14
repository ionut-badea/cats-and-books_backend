# Generated by Django 3.0.4 on 2020-04-04 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0043_remove_comment_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='articles',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='articles', to='posts.Tag'),
        ),
    ]