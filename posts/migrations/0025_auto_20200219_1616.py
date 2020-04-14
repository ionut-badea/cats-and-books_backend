# Generated by Django 3.0.3 on 2020-02-19 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_auto_20200219_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(blank=True, db_column='article', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.Article'),
        ),
    ]