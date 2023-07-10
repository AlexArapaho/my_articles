# Generated by Django 4.1.6 on 2023-07-09 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0002_delete_feedback'),
        ('articles', '0003_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='title',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
        migrations.CreateModel(
            name='PostFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles')),
                ('commentator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readers.profile')),
            ],
        ),
    ]