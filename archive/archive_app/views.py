from django.shortcuts import render, redirect,get_object_or_404, get_list_or_404
from .models import Question
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader, RequestContext
from .forms import QuestionForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def user_register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        if User.objects.filter(username=['username']).exists():
            return redirect('user_register')
        form.save()
        return redirect('user_login')
    return render(request, 'register.html', {'form': form})

def user_login(request):
    context= {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Provide Valid Credentials!!"
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)

@login_required
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "success.html", context)

def user_logout(request):
    if request.method == "POST":
        logout(request)
    return HttpResponseRedirect(reverse('user_login'))

@login_required
def list_questions(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {
        'questions': questions
    })

@login_required
def create_question(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():

        if Question.objects.filter(questionLink=request.POST['questionLink']).exists():
            return redirect('create_questions')
        else:
            f = form.save(commit=False)
            f.addedBy = request.user
            f.save()
            return redirect('list_questions')

    return render(request, 'questions-form.html', {'form': form})

@login_required
def update_question(request, id):
    try:
        question =get_object_or_404( Question,pk=id)
    except:
        return HttpResponse("id does not exist")  
    else:      
        form = QuestionForm(request.POST or None, instance=question)

        if form.is_valid():
            form.save()
            return redirect('list_questions')

    return render(request, 'questions-form.html', {'form': form, 'question': question})

@login_required
def delete_question(request, id):
    try:
        question =get_object_or_404( Question,pk=id)
    except:
        return HttpResponse("id does not exist")  
   
    else:
       if request.method == 'POST':
           question.delete()
           return redirect('list_questions')

       return render(request, 'ques-delete-confirm.html', {'question': question})