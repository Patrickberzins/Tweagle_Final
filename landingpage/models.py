from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ReportA(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='report_user', on_delete=models.CASCADE)
    description = models.TextField()
    

    def __str__(self):
        return self.title + ' | by ' + str(self.author)

    def get_absolute_url(self):
        return reverse('report_success')



# Create your models here.
