from django.shortcuts import render, redirect
from .models import Question
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader, RequestContext
from .forms import QuestionForm

# Create your views here.
def list_questions(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {
        'questions': questions
    })

def create_question(request):
    form = QuestionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_questions')

    return render(request, 'questions-form.html', {'form': form})

def update_question(request, id):
    question = Question.objects.get(id=id)
    form = QuestionForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect('list_questions')

    return render(request, 'questions-form.html', {'form': form, 'question': question})

def delete_question(request, id):
    question=Question.objects.get(id=id)

    if request.method == 'POST':
        question.delete()
        return redirect('list_questions')

    return render(request, 'ques-delete-confirm.html', {'question': question})