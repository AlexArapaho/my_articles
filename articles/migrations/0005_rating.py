# Generated by Django 4.1.6 on 2023-08-09 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0004_remove_articles_rating_articles_average_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, choices=[(1, 'Отвратительно'), (2, 'Плохо'), (3, 'Так себе'), (4, 'Неплохо'), (5, 'Отлично!')], default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
