from django.conf.urls import patterns, include, url

from demo.views import Demo, get_graphy
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'charts.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^demo/$', Demo.as_view()),
                       url(r'^get-graphy/$', get_graphy.as_view(), name='get-graphy')
                       )
