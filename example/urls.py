from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template
import faq.views

admin.autodiscover()

urlpatterns = patterns('',
    url(regex = r'^faq/$',
        view  = faq.views.faq_list,
        name  = 'faq_list',
    ),
    url(regex = r'^grouped_faq/$',
        view  = faq.views.faq_list_by_group,
        name  = 'faq_list_by_group',
    ),
    url(regex = r'^submit_faq/$',
        view  = faq.views.submit_faq,
        name  = 'submit',
        ),
    url(regex = r'^raw_faq/$',
        view  = faq.views.question_list,
        name  = 'question_list',
        ),
    url(regex  = r'^$',
        view   = direct_to_template,
        kwargs = {'template': 'faq/home.html'},
        name   = 'home',
    ),
    
    url(r'^admin/(.*)', include(admin.site.urls)),

    # Normally we'd do this if DEBUG only, but this is just an example app.
    url(regex  = r'^static/(?P<path>.*)$', 
        view   = 'django.views.static.serve',
        kwargs = {'document_root': settings.MEDIA_ROOT}
    ),
)