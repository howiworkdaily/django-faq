from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from faq.managers import QuestionManager
import faq.enums as enums

class FaqBase(models.Model):
    """
    Base class for models.
    """
    created_by = models.ForeignKey(User, null=True, editable=False, related_name="%(class)s_created_by", verbose_name=_('created by'))
    created_on = models.DateTimeField(_('created on'), default=datetime.now, editable=False)
    updated_on = models.DateTimeField(_('updated on'), editable=False)
    updated_by = models.ForeignKey(User, null=True, editable=False, verbose_name=_('updated by'))

    class Meta:
        abstract = True

class Question(FaqBase):
    """
    Represents a frequently asked question.
    """
    slug = models.SlugField(_('slug'), max_length=100, help_text=_("This is a unique identifier that allows your questions to display its detail view, ex 'how-can-i-contribute'"))
    text = models.TextField(_('question'), help_text=_('The actual question itself.'))
    answer = models.TextField( _('answer'), help_text=_('The answer text.'))
    status = models.IntegerField(_('status'), choices=enums.QUESTION_STATUS_CHOICES, default=enums.STATUS_INACTIVE, help_text=_("Only questions with their status set to 'Active' will be displayed."))
    sort_order = models.IntegerField(_('sort order'), default=0, help_text=_('The order you would like the question to be displayed.'))

    objects = QuestionManager()

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')
        ordering = ('sort_order', 'created_on')

    def __unicode__(self):
        return self.text

    def save(self):
        self.updated_on = datetime.now()
        super(Question, self).save()
