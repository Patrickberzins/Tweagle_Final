from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, CreateView, TemplateView, UpdateView
from .models import Admin_FlagList, Post, Report, Comment
from .forms import FlagForm, PostForm, ReportForm, CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

#def home(request):
    #return render(request, 'home.html', {})

class MessageBoardView(ListView):
    model = Post
    template_name = 'message_board.html'
    ordering = ['-post_date', '-post_time']

class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'
    ordering = ['-post_date', '-post_time']

def SearchResults(request):
    if request.method == "POST":
        searched = request.POST['searched']
        tweets = Post.objects.filter(body__contains=searched)
        return render(request, 'search_results.html',{'searched':searched,'tweets':tweets})
    else:
        return render(request, 'search_results.html',{})

def SearchUserResults(request):
    if request.method == "POST":
        searched = request.POST['searched']
        try:
            userid = User.objects.get(username=searched).pk
        except User.DoesNotExist:
            userid = None

        if userid != None:
            tweets = Post.objects.filter(author_id=userid)
            return render(request, 'search_user_results.html',{'searched':searched,'tweets':tweets})
        else:
            return render(request, 'search_user_results.html',{'searched':searched})
    else:
        return render(request, 'search_user_results.html',{})

class MessageProfileView(ListView):
    model = Post
    template_name = 'usermessages.html'
    ordering = ['-post_date', '-post_time']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('message_board')

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        like_count = stuff.like_count()

        liked=False
        if (stuff.likes.filter(id=self.request.user.id).exists):
            liked = True
        
        context["liked"] = liked
        context["like_count"] = like_count
        return context

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if (post.likes.filter(id=request.user.id).exists()):
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('message_board')

class PostCreationView(CreateView):
    model = Post
    form_class = PostForm
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    template_name = 'post_creation.html'
    #fields = '__all__'
    #fields = ['author', 'body']

class CommentCreationView(CreateView):
    model = Comment
    form_class = CommentForm
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)
    template_name = 'comment_creation.html'
    success_url = reverse_lazy('message_board')
    #fields = '__all__'
    #fields = ['author', 'body']

class NewReportView(CreateView):
    model = Report
    form_class = ReportForm

    
    
    def form_valid(self,form):
        form.instance.byuser = self.request.user
        return super().form_valid(form)
    def event(request):
        context = {}
        target_user = request.post.get('author')
        context['touser'] = target_user
        return render(request, 'new_report.html', context)
    template_name = 'new_report.html'

class ReportedNoticeView(TemplateView):
    model = Report
    template_name = 'reported_notice.html'

class CreateSuccessView(TemplateView):
    model = Post
    template_name = 'create_success.html'


class AdminView(ListView):
    model = Post
    template_name = 'admin_view.html'
    ordering = ['-post_date', '-post_time'] 


class OkView (UpdateView):
    model = Post
    fields = ['admin_ok']
    template_name = 'post_update_form.html'
    success_url ="/admin_view"

class AddFlagView (CreateView):
    model = Admin_FlagList
    form_class = FlagForm
    template_name = 'add_flag.html'
    success_url ="/admin_view"

class DeleteUserView(DeleteView):
    model = Post
    template_name = 'delete_user.html'
    success_url = reverse_lazy('message_board')

    