# Generated by Django 4.1.6 on 2023-08-09 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
    ]
