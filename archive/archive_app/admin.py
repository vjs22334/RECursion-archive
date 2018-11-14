from django.contrib import admin
from .models import Question,Tag
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
   readonly_fields = ['addedOn','lastModified','addedBy']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
