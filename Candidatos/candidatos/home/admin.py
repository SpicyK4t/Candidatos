from django.contrib import admin
from home.models import Publicidad, Candidato, Compromiso, Noticia, GaleriaImagenes, ItemImagen, Video

class CandidatoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'tipo_candidato', 'partido_politico')
	list_filter = ('partido_politico', 'tipo_candidato' )
	fields = ('nombre', 'descripcion', 'fotografia', 'banner', 'estilo',
		'partido_politico', 'facebook', 'twitter', 'conoceme_foto', 
		'tipo_candidato', 'municipio', 'distrito', )
	#fieldsets = (
	#	("Personal", {'fields':('nombre', 'descripcion')}), 
	#)
class CompromisoAdmin(admin.ModelAdmin):
	list_display = ('candidato', 'texto')
	exclude = ('slug', )

class PublicidadAdmin(admin.ModelAdmin):
	exclude = ('slug', )

class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('candidato', 'titulo', 'destacada', 'fecha_publicacion')
	list_filter = ('fecha_publicacion', )
	exclude = ('slug', 'fecha_publicacion')

class GaleriaImagenesAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'candidato', )	
	exclude = ('slug', )

class ItemImagenAdmin(admin.ModelAdmin):
	list_display = ('galeria', 'slug')
	exclude = ('slug', 'texto', )

class VideoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'candidato')
	exclude = ('slug', )

# Register your models here.
admin.site.register(Publicidad, PublicidadAdmin)
admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Compromiso, CompromisoAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(GaleriaImagenes, GaleriaImagenesAdmin)
admin.site.register(ItemImagen, ItemImagenAdmin)
admin.site.register(Video, VideoAdmin)
