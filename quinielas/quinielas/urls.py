from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quinielas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'principal.views.index'),
    url(r'^jornada', 'principal.views.jornada'),
    url(r'^admin/', include(admin.site.urls)),
)
