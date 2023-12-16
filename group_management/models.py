from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='group_images/', blank=True, null=True)
    members = models.ManyToManyField(User, related_name='user_groups')
    moderators = models.ManyToManyField(User, related_name='moderated_groups', blank=True)

    def __str__(self):
        return self.name
