from django.conf.urls.defaults import patterns, include, url

from paest.pastebin.views import paste, detail

urlpatterns = patterns('', 
    url(r'^$', paste, name='paste'),
    url(r'^(?P<url>\w+)/$', detail, name='detail'),    
)                  
