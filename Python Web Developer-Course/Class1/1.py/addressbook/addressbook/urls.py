from django.conf.urls import patterns, include, url

from django.contrib import admin
import contacts.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',contacts.views.ListContactView.as_view(),name='contacts-list',),
    url(r'^new$', contacts.views.CreateContactView.as_view(),name='contacts-new',),
    url(r'edit/(?P<pk>\d+)/$',contacts.views.UpdateContactView.as_view(),name='contacts-edit'),
    url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(),name='contacts-delete'),
    url(r'^(?P<pk>\d+)/$', contacts.views.ContactView.as_view(),name='contacts-view',),
    url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(),name='contacts-delete'),
    url(r'^contacts-edit-addresses/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(), name='contacts-edit-addresses'),

    url(r'^edit/(?P<pk>\d+)/addresses$', contacts.views.EditContactAddressView.as_view(),
        name='contacts-edit-addresses',),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),

    url(r'^',include('restapi.urls')),

)
