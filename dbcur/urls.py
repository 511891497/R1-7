from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dbcur.views.home', name='home'),
    # url(r'^dbcur/', include('dbcur.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home.html$',"libdb.views.home"),
    url(r'^$',"libdb.views.home"),
    url(r'^search.html$',"libdb.views.search"),
    url(r'^delete.html/(\d+)$',"libdb.views.dele"),
    url(r'^detail.html/(\d+)$',"libdb.views.detail"),
    url(r'^add.html/',"libdb.views.add"),
    url(r'^update.html/(\d+)',"libdb.views.update"),
)
