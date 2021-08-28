from django.contrib import admin
from .models import Pregunta, SeleccionarRespuesta, PreguntasRespondidas, UsuarioJuego
from .forms import SeleccionarInLineFormset
# Register your models here.


class SeleccionarRespuestaInLine(admin.TabularInline):
	model = SeleccionarRespuesta
	opc_max = SeleccionarRespuesta.max_respuesta
	opc_min = SeleccionarRespuesta.min_respuesta
	formset = SeleccionarInLineFormset

class PreguntaAdmin(admin.ModelAdmin):
	model = Pregunta
	inlines = (SeleccionarRespuestaInLine, )
	list_display = ['texto',]
	search_fields = ['texto', 'preguntas__texto']


class PreguntasRespondidasAdmin(admin.ModelAdmin):
	list_display = ['pregunta', 'respuesta', 'correcta', 'puntaje']

	class Meta:
		model = PreguntasRespondidas


admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(SeleccionarRespuesta)
admin.site.register(PreguntasRespondidas)
admin.site.register(UsuarioJuego)