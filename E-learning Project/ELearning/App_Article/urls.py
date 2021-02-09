from django.urls import path
from . import views
app_name='App_Article'


urlpatterns = [
    path('',views.mainhome,name='home'),
    path('article_home/',views.home.as_view(),name='article_home'),
    path('post_article/',views.Createarticle.as_view(),name='post_article'),
    path('view_article/<slug>/',views.detail,name='view_article'),
]
