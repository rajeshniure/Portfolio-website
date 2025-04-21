# from django.db import models

# # Create your models here.

# class Profile(models.Model):
#     name = models.CharField(max_length=100)
#     role = models.CharField(max_length=100)
#     description = models.TextField()
#     cv = models.FileField(upload_to='cv/')
#     avatar = models.ImageField(upload_to='avatars/')
#     instagram = models.URLField(max_length=200)
#     linkedin = models.URLField(max_length=200)
#     github = models.URLField(max_length=200)

#     def __str__(self):
#         return self.name



from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    aboutDescription = models.TextField(default='This is my about section.')
    about_image = models.ImageField(upload_to='about_images/', default='about_images/default.jpg')
    cv = models.FileField(upload_to='cv/')
    avatar = models.ImageField(upload_to='avatars/')
    instagram = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    github = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/')  # Skill icon/image

    def __str__(self):
        return self.name








class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"




class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(max_length=500)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name




