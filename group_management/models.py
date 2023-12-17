from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='group_images/', blank=True, null=True)
    members = models.ManyToManyField(User, related_name='user_groups')
    moderators = models.ManyToManyField(User, related_name='moderated_groups', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
