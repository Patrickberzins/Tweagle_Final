from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from registration.models import Profile


class Admin_FlagList (models.Model):
    flaglist = models.CharField(max_length=100)

    def __str__(self):
        return self.flaglist 

    @classmethod
    def create(cls, flaglist):
        new_flag = cls(flaglist=flaglist)
        # do something with the book
        return new_flag


class Post(models.Model):
    title = models.CharField(max_length=500, default='Post')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='tweag_posts', default=None, blank=True, null=True)
    flagged = models.BooleanField(default=False)
    admin_ok = models.BooleanField(default=False)


    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('create-success')

    def print_list (self):
        array = []
        list = Admin_FlagList.objects.all()
        for i in range (len(list)):
            x = list[i].flaglist
            str(x)
            array.append(x)
            z = ', '
            z = z.join(array)
        return z

    def flag_check (self):
        flag_array=[]
        flag_set = Admin_FlagList.objects.all()
        for i in range (len(flag_set)):
            x = flag_set[i].flaglist
            str(x)
            flag_array.append(x)
        
        for substring in flag_array:
            if ((substring in self.body) and (self.admin_ok == False)):
                self.flagged = True
                self.save()
                return '!!! THIS POST HAS BEEN FLAGGED AS POTENTIALLY MISLEADING !!!'

            else:
                self.flagged = False
                self.save()
        return ''

    def print_users (self):
        user_array = []
        all_users = User.objects.all()
        for i in range (len(all_users)):
            x = all_users[i].username
            str(x)
            user_array.append(x)
            z = ', \n '
            z = z.join(user_array)
        return z

    def user_count (self):
        user_array = []
        all_users = User.objects.all()
        for i in range (len(all_users)):
            x = all_users[i].username
            str(x)
            user_array.append(x)
        return len(user_array)

    def message_today (self):
        today = datetime.date.today()
        post_array = []
        all_posts = Post.objects.all()
        for i in range (len(all_posts)):
            x = all_posts[i].post_date
            if (x == today):
                post_array.append(x)
        return len(post_array)

    def user_flag_count (self):
        array = []
        report_count = []
        all_posts = Post.objects.all()
        all_users = User.objects.all()
        for i in range (len(all_posts)):
            x = all_posts[i].flagged
            if (x == True and  self.admin_ok == False):
                for z in (all_users):
                    if (all_posts[i].author.username == z.username):
                        array.append (all_posts[i].author.username)
        for p in set(array):
            p = "{0} {1}".format(p,array.count(p))
            report_count.append(p)
            list = ', \n '
            list = list.join(report_count)
        return list


    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = "comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    comment_date = models.DateField(auto_now_add=True)
    comment_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.body, self.comment_body)


reason_choices = (
    ('hate', 'Contains Hate Speech'),
    ('fake', 'Contains Fake News'),
    ('threats', 'Contains Threats toward Others'),
)

class Report(models.Model):
    
    byuser = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
    touser = models.CharField(max_length=10, default='unknown')
    #touser = models.ForeignKey(User, related_name='created_for', on_delete=models.CASCADE)
    reason = models.CharField(max_length=100, choices=reason_choices, default='fake')
    description = models.TextField()

    

    def __str__(self):
        return 'user ' + self.touser + ' | reported by user ' + str(self.byuser)

    def get_absolute_url(self):
        return reverse('reported-notice')

# Create your models here.
