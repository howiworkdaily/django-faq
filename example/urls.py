from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template
from faq.views import faq_list, faq_list_by_group, question_list, submit_faq

admin.autodiscover()

urlpatterns = patterns('',

(r'^admin/(.*)', admin.site.root),
url (
    regex = r'^faq/$',
    view = faq_list,
    name = 'faq_list',
    ),
url (
    regex = r'^grouped_faq/$',
    view = faq_list_by_group,
    name = 'faq_list_by_group',
    ),
url (
    regex = r'^submit_faq/$',
    view = submit_faq,
    name = 'submit',
    ),
url (
    regex = r'^raw_faq/$',
    view = question_list,
    name = 'question_list',
    ),
url (
    r'^$',
    direct_to_template,
    {'template': 'faq/home.html'},
    name = 'home',
    ),
)

urlpatterns += patterns('',
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
