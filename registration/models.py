from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

class Email(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE )
    bio = models.TextField()
    title = models.TextField(max_length=50)
    profile_pic = models.ImageField(null = True, blank = True, upload_to = "profileimages")

    def __str__(self):
        return str(self.user)


