from django import forms
from .models import Question
from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['questionName', 'difficulty', 'questionLink', 'solutionLink', 'summary']
    def clean(self):
        cleaned_data = super(QuestionForm, self).clean()
        link = cleaned_data.get('questionLink')
        if Question.objects.filter(questionLink=link).exists():
            Q = Question.objects.get(questionLink=link)
            raise forms.ValidationError('Question Already exists: '+Q.questionName)
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']