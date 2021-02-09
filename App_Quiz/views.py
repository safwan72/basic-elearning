from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from django.urls import  reverse,reverse_lazy
from django.views.generic.list import ListView
from . import forms
from .models import Question,Quiz,PublishedQuiz
from django.conf import settings
from App_Login.decorators import user_role
from App_Login.models import Teacher
# Create your views here.

@user_role()
def quiz(request):
    question=forms.CreateQuestion()
    if request.method=='POST':
        question=forms.CreateQuestion(request.POST)
        if question.is_valid():
            question.save()
            return HttpResponseRedirect(reverse_lazy('App_Quiz:question'))
    return render(request,'App_Quiz/Question.html',context={'form':question})

@user_role()
def questions(request):
    question=Question.objects.filter(added_to_quiz=False)
    return render(request,'App_Quiz/Quiz.html',context={'form':question})

@user_role()
def add_question(request,pk):
    creator=get_object_or_404(Teacher,user=request.user)
    question=Question.objects.get(added_to_quiz=False,pk=pk)
    quiz=Quiz.objects.get_or_create(creator=creator,created=False)

    if quiz[0].created==False:
        quiz=quiz[0]
        quiz.quiz.add(question)
        question.added_to_quiz=True
        question.save()
        quiz.save()
        return HttpResponseRedirect(reverse('App_Quiz:question'))
    else:
        quiz=Quiz(creator=creator)
        quiz.quiz.add(question)
        question.added_to_quiz=True
        question.save()
        quiz.save()
        return HttpResponseRedirect(reverse('App_Quiz:question'))


@user_role()
def create_quiz(request):
    creator=get_object_or_404(Teacher,user=request.user)
    quiz=Quiz.objects.filter(creator=creator,created=False)
    if quiz.exists():
        quiz=quiz[0]
        quiz_questions=quiz.quiz.all()
        return render(request,'App_Quiz/PublishQuiz.html',context={'quiz_questions':quiz_questions})
    else:
        return HttpResponseRedirect(reverse('App_Quiz:quiz'))


    
@user_role()    
def published_quizes(request):
    creator=get_object_or_404(Teacher,user=request.user)
    quiz=Quiz.objects.get(creator=creator,created=False)
    published_quiz=PublishedQuiz.objects.get_or_create(quiz=quiz,published=False)[0]
    if published_quiz.published==False:                   
            quiz.created=True
            published_quiz.published=True
            quiz.save()
            published_quiz.save()
    return HttpResponseRedirect(reverse('App_Quiz:quiz'))
    
    
    
class AllQuizes(ListView,LoginRequiredMixin):
    template_name='App_Quiz/AllQuizes.html'
    model=PublishedQuiz
    context_object_name='quiz'