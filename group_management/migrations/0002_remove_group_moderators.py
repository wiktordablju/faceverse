# Generated by Django 5.0 on 2023-12-15 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='moderators',
        ),
    ]
