from django.conf.urls import url
from restapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^restapi/$', views.SnippetList.as_view()),
    #url(r'^restapi/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)