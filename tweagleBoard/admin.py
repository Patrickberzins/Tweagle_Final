from django.contrib import admin
from .models import Admin_FlagList, Post, Comment, Report

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Admin_FlagList)
admin.site.register(Report)



# Register your models here.
