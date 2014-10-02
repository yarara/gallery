from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import routers
from galleryapp.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = patterns('',
    
    url(r'^$', 'galleryapp.views.index'),
    url(r'^api/', include(router.urls)),
    url(r'^userdashboard/$', 'galleryapp.views.userdashboard'),
    url(r'^registration/$', 'galleryapp.views.registration'),
    url(r'^userdashboard/image/(?P<image_id>.*)/$', 'galleryapp.views.imagebrowse'),
    url(r'^login/$', 'galleryapp.views.login'),
    url(r'^logout/$', 'galleryapp.views.logout'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    ) + urlpatterns