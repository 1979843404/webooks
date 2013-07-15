from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^', include("webooks.urls.urls")),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^api/v0/', include("webooks.apis.urls")),
    url(r'^internal/', include("webooks.privates.urls")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^wx/', include("webooks.weixin.urls")),

    url(r'^admin/', include(admin.site.urls)),
)