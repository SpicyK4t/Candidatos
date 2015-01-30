from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'candidatos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',         include(admin.site.urls)),
    url(r'^$',             'home.views.inicio'),
    url(r'^inicio2/$',     'home.views.inicio2'),
    url(r'^candidato/(?P<n_candidato>[a-z-0-9]+)/$',                                      'home.views.candidato'),
    url(r'^candidato/(?P<n_candidato>[a-z-0-9]+)/conoceme/$',                             'home.views.perfil'),
    url(r'^candidato/(?P<n_candidato>[a-z-0-9]+)/compromisos/$',                          'home.views.compromisos'),
    url(r'^candidato/(?P<n_candidato>[a-z-0-9]+)/galerias/$',                             'home.views.galerias'),
    url(r'^candidato/(?P<n_candidato>[a-z-0-9]+)/galerias/(?P<i_galeria>[a-z-0-9]+)/$',   'home.views.galeria'),
    url(r'^candidato/(?P<n_candidato>[a-z-0-9]+)/noticias/$',                             'home.views.noticias'),
    url(r'^candidato/(?P<n_candidato>[a-z-0-9]+)/noticias/(?P<t_noticia>[a-z-0-9]+)/$',   'home.views.noticia'),
    url(r'^candidato/(?P<n_candidato>[a-z-0-9]+)/videos/$',                               'home.views.videos'),
    url(r'^candidato/(?P<n_candidato>[a-z-0-9]+)/videos/(?P<i_video>[a-z-0-9]+)/$',       'home.views.video'),
) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += patterns('',
(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
'document_root': settings.MEDIA_ROOT}))

