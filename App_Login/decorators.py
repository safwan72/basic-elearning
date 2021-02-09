from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy

def user_role():
    def decorator(view_fun):
        def wrap(request,*args,**kwargs):
            try:
                if not request.user.is_teacher:
                    return HttpResponseRedirect(reverse_lazy('App_Article:article_home'))
                else:
                    return view_fun(request,*args,**kwargs)
                
            except PermissionError:
                return HttpResponseRedirect(reverse_lazy('App_Article:article_home'))
        return wrap 
    return decorator