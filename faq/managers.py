from django.db import models
from django.db.models.query import QuerySet
import datetime
import enums


class QuestionQuerySet(QuerySet):
    """
    A basic ''QuerySet'' subclass, provides query functionality and some helper methods for an intuitive interface.
    
    """
    
    def active(self, **kwargs):
        """
        A utility method that filters results based on ''Question'' models that are only ''Active''.

        """
        group = False
        if kwargs.get('group'):
            group = kwargs['group']

        if kwargs.get('slug'):
            slug = kwargs['slug']
            return self.filter(status__exact=enums.STATUS_ACTIVE, slug__exact=slug)
        elif group:
            return self.exclude(status__exact=enums.STATUS_INACTIVE,)
        else:
            return self.filter(status__exact=enums.STATUS_ACTIVE,)


class QuestionManager(models.Manager):
    """
    A basic ''Manager'' subclass which returns a ''QuestionQuerySet''. It provides simple access to helpful utility methods.  
    """

    def get_query_set(self):
        return QuestionQuerySet(self.model)

    def active(self, slug=None, group=False, user=None ):
        qs = self.get_query_set().active(slug=slug,group=group)
        if not user or not user.is_authenticated():
            return qs.exclude(protected=True)
        return qs
