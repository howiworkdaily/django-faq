from django.conf.urls.defaults import *
from django.contrib import admin
from views import question_detail, question_list

admin.autodiscover()

urlpatterns = patterns('',

url (
    regex = r'^question/(?P<slug>[-\w]+)/$',
    view = question_detail,
    name = 'question_detail',
    ),

url (
    regex = r'^questions/$',
    view = question_list,
    name = 'question_list',
    ),

)

