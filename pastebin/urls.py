from django.conf.urls import url

from pastebin.views import paste, detail

urlpatterns = [
    url(r'^$', paste, name='paste'),
    url(r'^(?P<url>\w+)/$', detail, name='detail'),
    url(r'^(?P<url>\w+)/raw/$', detail, {'raw': True}, name='detail-raw'),
]
