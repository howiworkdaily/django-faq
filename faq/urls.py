from __future__ import absolute_import

from django.conf.urls.defaults import *
from . import views as faq_views

urlpatterns = patterns('',
    url(regex = r'^$',
        view  = faq_views.question_list,
        name  = 'faq_question_list',
    ),
    url(regex = r'^submit/$',
        view  = faq_views.submit_faq,
        name  = 'faq_submit',
    ),
    url(regex = r'^(?P<slug>[\w-]+)/$',
        view  = faq_views.question_detail,
        name  = 'faq_question_detail',
    ),
)