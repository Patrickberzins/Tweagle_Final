from django import forms
from .models import Post, Admin_FlagList, Report, Comment
from django.forms.fields import ChoiceField
from urllib import request

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        
        widgets = {
            #'title': form.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control new_post_box', 'placeholder': 'Penny for your thoughts.'}),
        }

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason','touser','description']
        
        widgets = {
            'reason': forms.Select(attrs={'class': 'form-control'}),
            'touser': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Reported User Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detailed Description of Violation'}),
        }

class FlagForm(forms.ModelForm):
    class Meta:
        model = Admin_FlagList
        fields = ['flaglist']

        widgets = {
            'flaglist': forms.Textarea(attrs={'class': 'form-control new_post_box', 'placeholder': 'Add a flag?'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body']
        
        widgets = {
            #'title': form.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'comment_body': forms.Textarea(attrs={'class': 'form-control new_post_box', 'placeholder': 'Add comment here.'}),
        }