# Generated by Django 3.0.3 on 2020-02-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20200220_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'default_related_name': 'messages', 'ordering': ['-created'], 'verbose_name': 'message', 'verbose_name_plural': 'messages'},
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.CharField(max_length=50, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='name'),
        ),
    ]