from django.urls import path
from . import views
from .views import WelcomeView, UserEditView


urlpatterns = [
    path('', views.index, name='registration'),
    path('welcome/', WelcomeView.as_view(), name = 'welcome'),
    path('profile/', UserEditView.as_view(), name = 'profile'),
]