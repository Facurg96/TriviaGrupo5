from django import forms
from .models import Pregunta, SeleccionarRespuesta, PreguntasRespondidas


class SeleccionarInLineFormset(forms.BaseInlineFormSet):
	def clean(self):
		super(SeleccionarInLineFormset, self).clean()

		respuesta_correcta = 0
		for formulario in self.forms:
			if not formulario.is_valid():
				return

			if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
				respuesta_correcta += 1

		try:
			assert respuesta_correcta == Pregunta.num_opciones_permit
		except AssertionError:
			raise forms.ValidationError('Solo se permite una respuesta')
