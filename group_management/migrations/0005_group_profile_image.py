# Generated by Django 5.0 on 2023-12-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_management', '0004_alter_group_moderators'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='group_images/'),
        ),
    ]