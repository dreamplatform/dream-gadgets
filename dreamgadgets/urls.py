
from django.conf.urls.defaults import *

urlpatterns = patterns('dreamgadgets.views',
    url(r'^kauniainen_services/?$', 'kauniainen_services', name='kauniainen_services'),
    url(r'^dreamschool_services/?$', 'dreamschool_services', name='dreamschool_services'),
    url(r'^video_service/?$', 'video_service', name='video_service'),
    url(r'^fisholution/?$', 'fisholution', name='fisholution'),
    url(r'^moodle/?$', 'moodle', name='moodle'),
    url(r'^wiki/?$', 'wiki', name='wiki'),
    url(r'^blogi/?$', 'blogi', name='blogi'),
    url(r'^unelmasalkku/?$', 'unelmasalkku', name='unelmasalkku'),
    url(r'^dropbox/?$', 'dropbox', name='dropbox'),
    url(r'^sporttigalaksi/?$', 'sporttigalaksi', name='sporttigalaksi'),
    url(r'^pelitehdas/?$', 'pelitehdas', name='pelitehdas'),
    url(r'^steinerkoulu_espoo/?$', 'steinerkoulu_espoo', name='steinerkoulu_espoo'),
    url(r'^steinerkoulu_espoo_services/?$', 'steinerkoulu_espoo_services', name='steinerkoulu_espoo_services'),
    url(r'^steinerkoulu_tampere/?$', 'steinerkoulu_tampere', name='steinerkoulu_tampere'),
    url(r'^steinerkoulu_tampere_services/?$', 'steinerkoulu_tampere_services', name='steinerkoulu_tampere_services'),
    url(r'^google_calendar/?$', 'google_calendar', name='google_calendar'),
    url(r'^google_drive/?$', 'google_drive', name='google_drive'),
    url(r'^innoomnia/?$', 'innoomnia', name='innoomnia'),
)