
from datetime import datetime

from django.contrib import admin
from django.contrib.contenttypes import generic

from faq.models import Question, QuestionAssociation

class QuestionGenericInline(generic.GenericStackedInline):
    model = Question
    ct_fk_field = "object_pk"
    fields = ("sort_order", "text", "answer", "status")
    extra = 2

class QuestionAssociationGenericInline(generic.GenericTabularInline):
    model = QuestionAssociation
    ct_fk_field = "object_pk"
    raw_id_fields = ("question",)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'sort_order', 'created_by', 'created_on', 'updated_by', 'updated_on', 'status']
    fieldsets = (
        (None, {
            "fields": ("slug", "text", "answer", "status", "sort_order"),
        }),
        
        ("Object Association", {
            "fields": ("content_type", "object_pk"),
        }),
    )

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
        
        return instance

admin.site.register(Question, QuestionAdmin)
