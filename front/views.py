from django.shortcuts import render_to_response, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import LogEntry
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from register.models import Cursos
from pensum.models import *
from front.models import *


@login_required(login_url='login')
def front(request):
	dat=request.user.grado
	cursos=Cursos.objects.get(nombre_curso=dat)
	materias=Materia.objects.filter(id_cursos=cursos.id)
	data={'materias':materias}
	return render_to_response('front/front.html',data,context_instance=RequestContext(request))

def fromMenu(request):
	curso=request.POST.get('uid')
	data={'curso':curso}
	return render_to_response('front/pages/front/cursos.html', data,context_instance=RequestContext(request))

def fromHerramienta(request):
	return render_to_response('front/pages/front/Herramientas.html', context_instance=RequestContext(request))

def fromNotas(request):
	return render_to_response('front/pages/front/Notas.html', context_instance=RequestContext(request))

def Logros(request):
	mate=request.POST.get('materia')
	materia=Materia.objects.get(id=mate)
	logro=Logro.objects.filter(id_materia=materia)
	data={'logro':logro}
	return render_to_response('front/pages/front/Logros.html', data, context_instance=RequestContext(request))	

def actividades(request):
	if 'logro' in request.POST:
		log=request.POST.get('logro')
	else:
		log=request.session.get('logro')
		del request.session['logro']

	logro=Logro.objects.get(id=log)
	actividad=Actividad.objects.filter(id_logro=logro.id,estado_envio=True)
	id_user=request.user.id
	usuario=User.objects.get(id=id_user)
	envio=Envio.objects.filter(id_estudiante=usuario)
	print actividad
	data={'actividad':actividad,'envio':envio}
	return render_to_response('front/pages/front/Actividades.html', data,context_instance=RequestContext(request))

def saveActividad(request):

	uid=request.POST.get('uid')
	actividad=Actividad.objects.get(id=uid)
	id_user=request.user.id
	usuario=User.objects.get(id=id_user)
	actividad.estado_envio=False
	actividad.save()
	nuevo_envio = Envio.objects.create(id_estudiante=usuario,id_actividad=actividad)


	if request.FILES:
		nuevo_envio.adjunto = request.FILES.get('adjunto')

	nuevo_envio.save()


	request.session['logro']=actividad.id_logro.id

	return redirect(reverse('actividades'))
