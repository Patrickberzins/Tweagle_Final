from django.urls import path
from .views import inbox, Directs, SendDirect, UserSearch, NewConversation

urlpatterns = [
    path('', inbox, name="inbox"),
    path('directs/<username>', Directs, name='directs'),
    path('send/', SendDirect, name='senddirect'),
    path('new/', UserSearch, name='usersearch'),
    path('new/<username>', NewConversation, name='newconversation'),
]
