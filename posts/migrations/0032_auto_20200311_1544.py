# Generated by Django 3.0.3 on 2020-03-11 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0031_auto_20200227_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='author',
            field=models.ForeignKey(db_column='author', default='1d15c2c3-0b49-4a72-bf81-676656303dfa', on_delete=django.db.models.deletion.DO_NOTHING, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(db_column='author', default='1d15c2c3-0b49-4a72-bf81-676656303dfa', on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tag',
            name='author',
            field=models.ForeignKey(db_column='author', default='1d15c2c3-0b49-4a72-bf81-676656303dfa', on_delete=django.db.models.deletion.DO_NOTHING, related_name='tags', to=settings.AUTH_USER_MODEL),
        ),
    ]