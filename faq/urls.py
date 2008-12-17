from django.conf.urls.defaults import *
<<<<<<< HEAD:faq/urls.py
from faq.views import question_detail, question_list

urlpatterns = patterns('',
    url(r'^question/(?P<slug>[-\w]+)/$', question_detail, 'question_detail'),
    url(r'^questions/$', question_list, 'question_list'),
)
=======
from django.contrib import admin
from faq.views import faq_list_by_group, submit_faq

admin.autodiscover()

urlpatterns = patterns('',

url (
    r'^$',
    faq_list_by_group,
    name = 'faq',
    ),
url (
    r'^submit_faq/$',
    submit_faq,
    {'success_url': '/faq/'},
    name = 'submit',
    ),
)

>>>>>>> 5103a3f9e904b2c0ee327ce6cf0b3894a046d42a:faq/urls.py
