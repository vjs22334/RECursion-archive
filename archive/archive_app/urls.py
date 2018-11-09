from django.urls import path
from .views import list_questions, create_question, update_question, delete_question


urlpatterns = [
    path('', list_questions ,name='list_questions'),
    path('new', create_question , name='create_questions'),
    path('update/<int:id>/', update_question, name='update_question'),
    path('delete/<int:id>/', delete_question, name='delete_question'),
]