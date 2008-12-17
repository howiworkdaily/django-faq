<<<<<<< HEAD:faq/admin.py
from datetime import datetime
from django.contrib import admin
from faq.models import Question

class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        'text',
        'sort_order',
        'created_by',
        'created_on',
        'updated_by',
        'updated_on',
        'status'
    )

    def save_model(self, request, obj, form, change): 
        """
        Overrided because I want to also set who created this instance.
        """
        instance = form.save(commit=False)
        if instance.id is None:
            new = True
            instance.created_by = request.user
        instance.updated_by = request.user
        instance.save()
=======
from django.contrib import admin
from models import Question
from datetime import datetime
            

class QuestionAdmin(admin.ModelAdmin):
  
    list_display = ['text', 'sort_order', 'created_by', 'created_on', 'updated_by', 'updated_on', 'status']

    def save_model(self, request, obj, form, change): 
        '''
        Overrided because I want to also set who created this instance.
        '''
        instance = form.save( commit=False )
        if instance.id is None:
            new = True
            instance.created_by = request.user
                
        instance.updated_by = request.user
        instance.save()
        
>>>>>>> 5103a3f9e904b2c0ee327ce6cf0b3894a046d42a:faq/admin.py
        return instance

admin.site.register(Question, QuestionAdmin)
