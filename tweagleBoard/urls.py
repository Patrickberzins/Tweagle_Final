from tweagleBoard.forms import FlagForm
from django.urls import path
from . import views
from .views import OkView, MessageBoardView, PostDetailView, LikeView, DeletePostView, PostCreationView, CreateSuccessView, AdminView, AddFlagView, NewReportView, ReportedNoticeView, MessageProfileView, CommentCreationView, SearchResultsView, SearchResults, SearchUserResults

urlpatterns = [
    #path('', views.home, name = 'home')
    path('message_board', MessageBoardView.as_view(), name = 'message_board'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post-detail'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name ='delete_post'),
    path('post_creation', PostCreationView.as_view(), name = 'post_creation'),
    path('create-success', CreateSuccessView.as_view(), name = 'create-success'),
    path('admin_view', AdminView.as_view(), name = 'admin_view'),
    path('post/<int:pk>/update_post', OkView.as_view(), name ='post_update_form'),
    path('admin_view/add_flag', AddFlagView.as_view(), name ='add_flag'),
    path('report_page', NewReportView.as_view(), name ='report_page'),
    path('reported_notice', ReportedNoticeView.as_view(), name = 'reported-notice'),
    path('usermessages', MessageProfileView.as_view(), name = 'usermessages'),
    path('search_results', views.SearchResults, name = 'search_results'),
    path('post/<int:pk>/comment', CommentCreationView.as_view(), name= 'comment_creation'),
    path('search_user_results', views.SearchUserResults, name = 'search_user_results'),

]
