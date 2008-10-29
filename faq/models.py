from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from faq.managers import QuestionManager
import faq.enums as enums

class FaqBase(models.Model):
    '''
    Base class for models.
    
    '''
    created_by = models.ForeignKey(User, null=True, editable=False, related_name="%(class)s_created_by" )    
    created_on = models.DateTimeField( _('created on'), default=datetime.now, editable=False,  )
    updated_on = models.DateTimeField( _('updated on'), editable=False )
    updated_by = models.ForeignKey(User, null=True, editable=False )  
    
    class Meta:
        abstract = True

class Question(FaqBase):
    """
    Represents a frequently asked question.

    """

    slug = models.SlugField( max_length=100, help_text="This is a unique identifier that allows your questions to display its detail view, ex 'how-can-i-contribute'", )
    text = models.TextField(_('question'), help_text='The actual question itself.')
    answer = models.TextField( _('answer'), help_text='The answer text.' )    
    status = models.IntegerField( choices=enums.QUESTION_STATUS_CHOICES, default=enums.STATUS_INACTIVE, help_text="Only questions with their status set to 'Active' will be displayed. " )
    sort_order = models.IntegerField(_('sort order'), default=0, help_text='The order you would like the question to be displayed.')
    
    # an object specific question
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_pk = models.PositiveIntegerField(null=True, blank=True)
    content_object = generic.GenericForeignKey(fk_field="object_pk")
    
    objects = QuestionManager()
    
    class Meta:
        ordering = ['sort_order', 'created_on', ]

    def __unicode__(self):
        return self.text

    def save(self):
        self.updated_on = datetime.now()
        super(Question, self).save()

class QuestionAssociation(models.Model):
    """
    A generic relation between a Question and some other object in the system.
    """
    question = models.ForeignKey(Question)
    content_type = models.ForeignKey(ContentType)
    object_pk = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey(fk_field="object_pk")
