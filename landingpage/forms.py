from django import forms
from .models import Profile
from django.forms.fields import ChoiceField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', max_length=50, required=True,)
    email = forms.EmailField(label='Email',required=True)
    
    TITLE= [
    ('Student', 'Student'),
    ('Faculty', 'Faculty'),
    ('Staff', 'Staff'),
    ]
    title=forms.CharField(label='Title', widget=forms.RadioSelect(choices=TITLE), required=False)
    bio = forms.CharField(label='Bio', widget=forms.Textarea, required=False)

    def clean_email(self):
        data = self.cleaned_data['email']
        if "@bc.edu" not in data:   # any check you need
            raise forms.ValidationError("!!! Invalid: Must be a BC email address !!!")
        return data

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "title", "bio",)


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', max_length=50, required=True)
    email = forms.EmailField(label='Email',widget = forms.TextInput(attrs={'readonly': 'readonly'}), required=True)
    username = forms.CharField(label='Username', max_length=50, required=True)
    bio = forms.CharField(label='Bio', widget=forms.Textarea)
    
    class Meta:
        model=Profile
        fields = ('username', 'first_name', 'last_name', 'email', 'bio')
