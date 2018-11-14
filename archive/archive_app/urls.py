from django.urls import path
from .views import *


urlpatterns = [
    path('', list_questions ,name='list_questions'),
    path('new_question', create_question , name='create_questions'),
    path('update/<int:id>/', update_question, name='update_question'),
    path('delete/<int:id>/', delete_question, name='delete_question'),
    path('new_tag',create_tag,name='create_tag'),
    path('list_tags',list_tags,name='list_tags'),

    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('register/', user_register, name="user_register"),
    path('accounts/login/', user_login, name="user_login"),
]