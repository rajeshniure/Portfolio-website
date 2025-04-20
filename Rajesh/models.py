from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    cv = models.FileField(upload_to='cv/')
    avatar = models.ImageField(upload_to='avatars/')
    instagram = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    github = models.URLField(max_length=200)

    def __str__(self):
        return self.name
