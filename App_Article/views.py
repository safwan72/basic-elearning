from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import  TemplateView,UpdateView,CreateView,DetailView,DeleteView,ListView
from . import  models,forms
from django.urls import  reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import  LoginRequiredMixin
import uuid
from App_Login.decorators import user_role

# Create your views here.
@login_required
def mainhome(request):
    return render(request,'Home.html',context={})

class home(ListView,LoginRequiredMixin):
    model=models.Article
    context_object_name='articles'
    template_name='App_Article/Home.html'

@login_required
def detail(request,slug):
    article=models.Article.objects.get(slug=slug)
    commentform=forms.CommentForm()
    if request.method=='POST':
        commentform=forms.CommentForm(request.POST)
        if commentform.is_valid():
            comment=commentform.save(commit=False)
            comment.user=request.user
            comment.article=article
            comment.save()
    return render(request,'App_Article/Detail.html',context={'article':article,'form':commentform})
    
    


class Createarticle(LoginRequiredMixin,CreateView):
    model=models.Article
    template_name='App_Article/NewArticle.html'
    fields=('title','content','article_image')
    
    def form_valid(self, form):
        article_obj=form.save(commit=False)
        article_obj.author=self.request.user.teacher
        title=article_obj.title
        article_obj.slug=title.replace(" ","-")+"-"+str(uuid.uuid4())
        article_obj.save()
        return HttpResponseRedirect(reverse('App_Article:home'))

