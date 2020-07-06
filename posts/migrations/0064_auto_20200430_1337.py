# Generated by Django 3.0.4 on 2020-04-30 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0063_auto_20200430_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, db_column='category', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='articles', to='posts.Category'),
        ),
    ]
