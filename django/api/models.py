from django.db import models


def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.title), filename])


class User(models.Model):
    user = models.CharField(max_length=255)
    pwd = models.CharField(max_length=255)


class Profile(models.Model):
    user = models.CharField(max_length=255)
    pwd = models.CharField(max_length=255)


class Image(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.CharField(blank=False, max_length=255
                            )
