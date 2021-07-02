from registration.forms import UserForm
from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic
from django.contrib.auth.forms import ReadOnlyPasswordHashWidget, UserCreationForm
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Report, Profile
from django.views.generic import ListView
from tweagleBoard.models import Post


#def index (request):
    #context ={}
    #context['form']= UserForm()
    #return render(request, 'index.html', context)

class UserRegisterView(generic.CreateView):
    form_class = UserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            request.user.first_name = form.cleaned_data.get ('firstname')
            request.user.last_name = form.cleaned_data.get ('lastname')
            user = authenticate(username=username, password=raw_password)
            Profile.objects.create(
                user=user,
                bio=form.cleaned_data['bio'], 
                title=form.cleaned_data['title'],)
            return redirect('welcome')
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})

def save(self, commit=True):

        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data["firstname"]
        user.last_name = self.cleaned_data["lastname"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user

class WelcomeView(ListView):
    model = Report
    template_name = "welcome.html"

class UserEditView(generic.UpdateView):
    form_class = ProfileForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('message_board')

    def get_object(self):
        return self.request.user

class MessageBoardView(ListView):
    model = Post
    template_name = 'registration/profile.html'
    ordering = ['-post_date']
    
    def get_object(self):
        return self.request.user
