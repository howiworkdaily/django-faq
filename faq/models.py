from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from managers import QuestionManager
import enums

class Question(models.Model):
    """
    Represents a frequently asked question.

    """

    slug = models.SlugField( max_length=100 )
    text = models.TextField(_('question'), help_text='The actual question itself.')
    status = models.IntegerField( choices=enums.QUESTION_STATUS_CHOICES, default=enums.STATUS_INACTIVE )
    created_by = models.ForeignKey(User, null=True, editable=False )    
    created_on = models.DateTimeField( _('created on'), default=datetime.now, editable=False )
    updated_on = models.DateTimeField( _('updated on'), editable=False )
    objects = QuestionManager()

    def __unicode__(self):
        return self.text

    def save(self):
        self.updated_on = datetime.now()
        super(Question, self).save()
        

class Answer(models.Model):
    """
    Represents an answer to a frequently asked question.

    """
    
    question = models.ForeignKey(Question, unique=True)
    slug = models.SlugField( max_length=100 )
    text = models.TextField( _('answer'), help_text='The answer text.' )
    created_by = models.ForeignKey( User, null=True, editable=False )    
    created_on = models.DateTimeField( _('created on'), default=datetime.now, editable=False )
    updated_on = models.DateTimeField( _('updated on'), editable=False )

    def __unicode__(self):
        return self.text
        
    def save(self):
        self.updated_on = datetime.now()
        super(Answer, self).save()
