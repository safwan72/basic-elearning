from django.db import models
from django.conf import settings
from App_Login.models import Teacher,Student

# Features Include: Categories of written articles, Question Answer Section, Quiz Section. Also, there will be two types of accounts: Student and Teacher.

# Create your models here.

class Article(models.Model):
    author=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='article_author')
    title=models.CharField(max_length=264,verbose_name='Put A Title')
    slug=models.SlugField(max_length=264,unique=True)
    content=models.TextField(verbose_name='Write Article Contents Here..')
    article_image=models.ImageField(verbose_name='Choose an Image',upload_to='article_images')
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=('-publish_date',)
        verbose_name_plural='Article'
        db_table = 'Article'
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,related_name='article_comment')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_comment')
    comment=models.TextField()
    comment_date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='Comment'
        db_table = 'Comment'
    
    def __str__(self):
        return self.comment