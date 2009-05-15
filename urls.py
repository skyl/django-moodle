from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import os
from settings import LIVE, PROJECT_DIR

if not LIVE:
    urlpatterns = patterns('',\
            (r'^media/(?P<path>.*)$', 'django.views.static.serve',\
                {'document_root': os.path.join(PROJECT_DIR, 'media/')}),

            (r'^admin_media/(?P<path>.*)$', 'django.views.static.serve',\
                {'document_root': os.path.join(PROJECT_DIR, 'admin_media/')}),
    )
else:
    urlpatterns = patterns('',)


urlpatterns += patterns('',
    # Example:
    # (r'^test_app/', include('test_app.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'views.home', name="home"),
    (r'^admin/', include(admin.site.urls)),
)
