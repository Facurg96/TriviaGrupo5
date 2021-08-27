from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Usuario(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	puntaje_total = models.DecimalField(verbose_name='Puntaje global obtenido',default=0, decimal_places=2, max_digits=8)



class Pregunta(models.Model):

	texto = models.TextField(verbose_name='Desarrollo de la pregunta')
	num_opciones_permit = 1

	def __str__(self):
		return self.texto


class SeleccionarRespuesta(models.Model):

	pregunta = models.ForeignKey(Pregunta, related_name='preguntas', on_delete= models.CASCADE)
	correcta = models.BooleanField(verbose_name= 'Respuesta Correcta', default= False, null= False)
	desarrollo = models.TextField(verbose_name='Desarrollo de la respuesta')
	max_respuesta = 3
	min_respuesta = 2
	def __str__(self):
		return self.desarrollo


class PreguntasRespondidas(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	respuesta = models.ForeignKey(SeleccionarRespuesta,on_delete=models.CASCADE, related_name='intentos')
	correcta = models.BooleanField(verbose_name= 'Respuesta correcta', default= False, null= False)
	puntaje = models.DecimalField(verbose_name= 'Puntos obtenidos', default=0, decimal_places=2, max_digits=8)
