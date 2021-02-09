from django.urls import path
from . import views

app_name='App_Quiz'

urlpatterns = [
    path('quiz/',views.quiz,name='quiz'),
    path('question/',views.questions,name='question'),
    path('add_question/<pk>/',views.add_question,name='add_question'),
    path('create_quiz/',views.create_quiz,name='create_quiz'),
    path('publish_quiz/',views.published_quizes,name='publish_quiz'),
    path('allQuizes/',views.AllQuizes.as_view(),name='allQuizes'),
]
