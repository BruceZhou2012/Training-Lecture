from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from cmdb.views import CMDBViews, SnippetList

router = DefaultRouter()
router.register(r'data', CMDBViews, base_name='data')

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^client/(?P<username>.+)/$', SnippetList.as_view()),
                       )
