from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroForm, UsuarioLoginFormulario
from django.contrib.auth import authenticate, login, logout
from .models import UsuarioJuego, Pregunta, PreguntasRespondidas



def inicio(request):

	ctx = {

		'bienvenido': 'Bienvenido'


	}


	return render(request, 'inicio.html', ctx)

def registro(request):

	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			form.save()
			#form = RegistroForm()
			return redirect('login')

	else:
		form = RegistroForm()

	context = {

		'form': form

	}

	return render(request, 'Usuario/registro.html', context)

def loginVista(request):
	titulo = 'login'
	form = UsuarioLoginFormulario(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		usuario = authenticate(username=username, password= password)
		login(request, usuario)
		return redirect('home')

	context = {
		'form':form,
		'titulo':titulo

	}

	return render(request, 'Usuario/login.html', context)


def logoutVista(request):
	logout(request)
	return redirect('/')


def HomeUsuario(request):
	return render(request, 'Usuario/home.html')


def resultado_pregunta(request, pregunta_respondida_pk):
	respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

	context = {
		'respondida':respondida
	}
	return render(request, 'Jugar/resultados.html', context)



def Jugar(request):
	UserJuego, created = UsuarioJuego.objects.get_or_create(usuario=request.user)

	if request.method == 'POST':
		pregunta_pk = request.POST.get('pregunta_pk')
		pregunta_respondida = UserJuego.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
		respuesta_pk = request.POST.get('respuesta_pk')

		try: 
			opcion_seleccionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
		except ObjectDoesNotExist:
			raise Http404

		UserJuego.validar_intento(pregunta_respondida, opcion_seleccionada)
		return redirect('resultado_pregunta', pregunta_respondida.pk)

	else:
		pregunta = UserJuego.nuevas_preguntas()
		if pregunta is not None:
			UserJuego.crear_intentos(pregunta)

		context = {
			'pregunta':pregunta

		}

	return render(request, 'Jugar/jugar.html', context)


def tablero(request):
	total_usuario_juego = UsuarioJuego.objects.order_by('-puntaje_total')
	contador = total_usuario_juego.count()

	context = {
		'usuario_juego':total_usuario_juego,
		'contar_user':contador
	}

	return render(request, 'Jugar/tablero.html', context)