from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import random


class UsuarioJuego(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	puntaje_total = models.DecimalField(verbose_name='Puntaje total',default=0, decimal_places=2, max_digits=8)

	def nuevas_preguntas(self):
		respondidas = PreguntasRespondidas.objects.filter(userJuego=self).values_list('pregunta__pk', flat=True)
		restantes = Pregunta.objects.exclude(pk__in=respondidas)
		if not restantes.exists():
			return None
		return random.choice(restantes)

	
	def crear_intentos(self, pregunta):
		intento = PreguntasRespondidas(pregunta=pregunta, userJuego=self)
		intento.save()


	def validar_intento(self, pregunta_respondida, respuesta_selecionada):
		if pregunta_respondida.pregunta_id != respuesta_selecionada.pregunta_id:
			return

		pregunta_respondida.respuesta_selecionada = respuesta_selecionada
		if respuesta_selecionada.correcta is True:
			pregunta_respondida.correcta = True
			pregunta_respondida.puntaje_obtenido = respuesta_selecionada.pregunta.max_puntaje
			pregunta_respondida.respuesta = respuesta_selecionada

		else:
			pregunta_respondida.respuesta = respuesta_selecionada

		pregunta_respondida.save()
		self.actualizar_puntaje()

	def actualizar_puntaje(self):
		puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(models.Sum('puntaje_obtenido'))['puntaje_obtenido__sum']

		self.puntaje_total = puntaje_actualizado
		self.save()


class Pregunta(models.Model):

	texto = models.TextField(verbose_name='Desarrollo de la pregunta')
	num_opciones_permit = 1
	max_puntaje = models.DecimalField(verbose_name='Máximo Puntaje', default=3, decimal_places=2, max_digits=5)

	def __str__(self):
		return self.texto


class SeleccionarRespuesta(models.Model):

	pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete= models.CASCADE)
	correcta = models.BooleanField(verbose_name= 'Respuesta Correcta', default= False, null= False)
	desarrollo = models.TextField(verbose_name='Desarrollo de la respuesta')
	max_respuesta = 3
	min_respuesta = 2
	def __str__(self):
		return self.desarrollo



class PreguntasRespondidas(models.Model):
	userJuego = models.ForeignKey(UsuarioJuego, on_delete=models.CASCADE, related_name='intentos')
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	respuesta = models.ForeignKey(SeleccionarRespuesta,on_delete=models.CASCADE, null=True)
	correcta = models.BooleanField(verbose_name= 'Respuesta correcta', default= False, null= False)
	puntaje_obtenido = models.DecimalField(verbose_name= 'Puntaje Obtenido', default=0, decimal_places=2, max_digits=8)

