from django.urls import path
from .views import OldHomeView, ReportPageView, ReportSuccessView
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.home, name="home"),
    path('oldhome/', OldHomeView.as_view(), name="oldhome"),
    path('', auth_views.LoginView.as_view(template_name='newhome.html'), name='home'),
    path('oldreport/', ReportPageView.as_view(), name="old_report_page"),
    path('report_success/', ReportSuccessView.as_view(), name="report_success")
]
