# Generated by Django 3.0.4 on 2020-04-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True, verbose_name='full name'),
        ),
    ]
