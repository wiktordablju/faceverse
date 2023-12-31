# Generated by Django 4.2.7 on 2023-12-11 06:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('members', models.ManyToManyField(related_name='user_groups', to=settings.AUTH_USER_MODEL)),
                ('moderators', models.ManyToManyField(related_name='moderated_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
