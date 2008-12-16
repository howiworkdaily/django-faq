from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from views import faq_list

admin.autodiscover()

urlpatterns = patterns('',

(r'^admin/(.*)', admin.site.root),
url (
    regex = r'^faq/$',
    view = faq_list,
    name = 'faq_list',
    ),

(r'^faq/(.*)', include('faq.urls'))

)


urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
)
