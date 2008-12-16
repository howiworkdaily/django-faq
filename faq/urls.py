from django.conf.urls.defaults import *
from faq.views import question_detail, question_list

urlpatterns = patterns('',
    url(r'^question/(?P<slug>[-\w]+)/$', question_detail, 'question_detail'),
    url(r'^questions/$', question_list, 'question_list'),
)
