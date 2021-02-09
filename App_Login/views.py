from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from . import models,forms


from django.contrib import messages
# Create your views here.


def student_profile_change(request):
    user=request.user
    profile=models.Student.objects.get(user=user)
    form=forms.StudentChangeForm(instance=profile)
    if request.method=='POST':
        form=forms.StudentChangeForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Updated Successfully')
            form=forms.StudentChangeForm(instance=profile)
            return HttpResponseRedirect(reverse('App_Login:s_profile'))
    
    return render(request,'App_Login/ProfileChange.html',context={'form':form})


def teacher_profile_change(request):
    user=request.user
    profile=models.Teacher.objects.get(user=user)
    form=forms.TeacherChangeForm(instance=profile)
    if request.method=='POST':
        form=forms.TeacherChangeForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Updated Successfully')
            form=forms.TeacherChangeForm(instance=profile)
            return HttpResponseRedirect(reverse('App_Login:t_profile'))
    
    return render(request,'App_Login/ProfileChange.html',context={'form':form})


def student_signupview(request):
    form=forms.StudentRegForm()
    if request.method=='POST':
        form=forms.StudentRegForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_student=True
            user.save()
            student=models.Student(user=user)
            student.save()
            messages.success(request,'Account Created Successfully')
            return HttpResponseRedirect(reverse('App_Article:home'))
    return render(request,'App_Login/Signup.html',context={'form':form,'title':'Student SignUp'})



def login_view(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Article:home'))
            messages.success(request,'Logged in Successfully')
        else:
            messages.warning(request,'Log In Failed. Check Proper Inputs')
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request,'App_Login/Login.html',context={'title':'Login Page','form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Article:home'))


def teacher_signupview(request):
    form=forms.TeacherRegForm()
    if request.method=='POST':
        form=forms.TeacherRegForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_teacher=True
            user.save()
            teacher=models.Teacher(user=user)
            teacher.save()
            messages.success(request,'Account Created Successfully')
            return HttpResponseRedirect(reverse('App_Article:home'))
    return render(request,'App_Login/Signup.html',context={'form':form,'title':'Teacher SignUp'})
    
   