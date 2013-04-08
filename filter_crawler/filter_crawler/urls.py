from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from account.views import logout_page
from filter_search.views import fetch

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'filter_crawler.views.home', name='home'),
    # url(r'^filter_crawler/', include('filter_crawler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    (r'^search', direct_to_template, {"template": "index.html"}),
    (r'^fetch', fetch),
    (r'^$', 'django.contrib.auth.views.login'),
    (r'^account/logout', logout_page),

)

