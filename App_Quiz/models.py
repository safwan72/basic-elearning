from django.db import models
from App_Login.models import Teacher,Student

# Create your models here.

class Question(models.Model):
    ques=models.CharField(max_length=264)
    option1=models.CharField(max_length=264)
    option2=models.CharField(max_length=264)
    option3=models.CharField(max_length=264)
    option4=models.CharField(max_length=264)
    correct_ans=models.CharField(max_length=264)
    added_to_quiz=models.BooleanField(default=False)
    
    class Meta:
        db_table='Question'
        verbose_name_plural='Question'




class Quiz(models.Model):
    creator=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='quiz_creator')
    participiants=models.ManyToManyField(Student,blank=True)
    quiz=models.ManyToManyField(Question)
    created=models.BooleanField(default=False)
    created_at_date=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        db_table='Quiz'
        verbose_name_plural='Quiz'

    
    
class PublishedQuiz(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='quiz_published')
    total_attendees=models.ManyToManyField(Student,blank=True)
    quiz_marks=models.IntegerField(blank=True,null=True)
    published=models.BooleanField(default=False)
    
    class Meta:
        db_table='Published_Quizes'
        verbose_name_plural='Published_Quizes'