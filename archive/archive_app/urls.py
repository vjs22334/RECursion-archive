from django.urls import path
from .views import list_questions, create_question, update_question, delete_question, user_login, user_register, user_logout, success


urlpatterns = [
    path('', list_questions ,name='list_questions'),
    path('new', create_question , name='create_questions'),
    path('update/<int:id>/', update_question, name='update_question'),
    path('delete/<int:id>/', delete_question, name='delete_question'),

    path('login/', user_login, name="user_login"),
    path('success/', success, name="user_success"),
    path('logout/', user_logout, name="user_logout"),
    path('register/', user_register, name="user_register"),
    path('accounts/login/', user_login, name="user_login"),
]