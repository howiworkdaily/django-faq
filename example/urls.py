from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin; admin.autodiscover()
from django.conf import settings
from django.views.generic import TemplateView
import faq.views

urlpatterns = patterns('',
    # Just a simple example "home" page to show a bit of help/info.
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    
    # This is the URLconf line you'd put in a real app to include the FAQ views.
    url(r'^faq/', include('faq.urls')),
    
    # Everybody wants an admin to wind a piece of string around.
    url(r'^admin/', include(admin.site.urls)),

    # Normally we'd do this if DEBUG only, but this is just an example app.
    url(regex  = r'^static/(?P<path>.*)$', 
        view   = 'django.views.static.serve',
        kwargs = {'document_root': settings.MEDIA_ROOT}
    ),
)