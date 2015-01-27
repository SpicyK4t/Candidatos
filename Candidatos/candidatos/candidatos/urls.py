from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'candidatos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',         include(admin.site.urls)),
    url(r'^$',             'home.views.inicio'),
    url(r'^inicio2/$',     'home.views.inicio2'),
    url(r'^candidato/$',   'home.views.candidato'),
    url(r'^conoceme/$',    'home.views.perfil'),
    url(r'^compromisos/$', 'home.views.compromisos'),
    url(r'^galerias/$',    'home.views.galerias'),
    url(r'^galeria/$',     'home.views.galeria'),
    url(r'^noticias/$',    'home.views.noticias'),
    url(r'^noticia/$',     'home.views.noticia'),
    url(r'^videos/$',      'home.views.videos'),
    url(r'^video/$',       'home.views.video'),
)
