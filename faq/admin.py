from django.contrib import admin
from models import Question, Answer
from datetime import datetime

class QuestionAdmin(admin.ModelAdmin):

    list_display = ['text', 'created_by', 'created_on','updated_on', 'status']

    def save_model(self, request, obj, form, change): 
        instance = form.save( commit=False )
        instance.created_by = request.user
        instance.save()
        return instance

class AnswerAdmin(admin.ModelAdmin):

    list_display = ['id', 'text', 'question', 'created_by', 'created_on','updated_on',]

    def save_model(self, request, obj, form, change): 
        instance = form.save( commit=False )
        instance.created_by = request.user
        instance.save()
        return instance
            
admin.site.register(Answer, AnswerAdmin)                
admin.site.register(Question, QuestionAdmin)