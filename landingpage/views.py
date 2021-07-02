from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.contrib.auth import login, authenticate
from .models import ReportA

# Create your views here.

#def home(request):
#    return render(request, 'home.html', {})

class OldHomeView(ListView):
    model = ReportA
    template_name = 'oldhome.html'


class ReportPageView(CreateView):
    model = ReportA
    template_name = 'report_page.html'
    fields = '__all__'

class ReportSuccessView(TemplateView):
    model = ReportA
    template_name = 'report_success.html'