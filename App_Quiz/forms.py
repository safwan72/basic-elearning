from django import forms
from . import models

class CreateQuestion(forms.ModelForm):
    class Meta:
        model=models.Question
        exclude=('added_to_quiz',)

