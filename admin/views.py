#encoding: utf-8
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
from register.models import *
from pensum.models import *
from control.models import *
from custom.models import *



def admin_login(request):

	if request.user.is_authenticated():
		return redirect(reverse('index'))

	if request.method == 'GET':
		form = AuthenticationForm(request)

		return render_to_response(
			'examples/login.html',
			{'form':form},
      		context_instance=RequestContext(request)
	    )

	elif request.method == 'POST':

		form = AuthenticationForm(request.POST)

		username = request.POST.get('username')
		password = request.POST.get('password')

		form.fields['username'].initial = username

		if not username:
			form_err = {'username_errors':'Ingresa un nombre de usuario'}
			return render_to_response(
				'examples/login.html',
				{'form':form, 'form_err':form_err},
				context_instance=RequestContext(request)
			)
		if not password:
			form_err = {'password_errors':'Ingresa una contraseña'}
			return render_to_response(
				'examples/login.html',
				{'form':form, 'form_err':form_err},
				context_instance=RequestContext(request)
			)

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				if user.rol=="estudiante":
					
					return redirect(reverse('front'),context_instance=RequestContext(request))
				else:
					return redirect(reverse('index'),context_instance=RequestContext(request))
			else:
				form_err = {}
				form_err['error'] = 'Esta cuenta está deshabilitada'

				return render_to_response(
					'examples/login.html',
					{'form':form, 'form_err':form_err},
					context_instance=RequestContext(request)
				)
		else:
			form_err = {}
			form_err['error'] = 'Esta cuenta no existe o la contraseña no coincide'
			return render_to_response(
				'examples/login.html',
				{'form':form, 'form_err':form_err},
				context_instance=RequestContext(request)
			)

def admin_logout(request):
	if not request.user.is_authenticated():
		return redirect('login')
	logout(request)
	return render_to_response('examples/login.html', context_instance=RequestContext(request))


@login_required(login_url='login')
def index (request):
	#Contar registros
	value=len(User.objects.filter(rol=""))
	mat=len(Cursos.objects.all())
	registro=value+mat
	#Contar estudiantes
	est=len(User.objects.filter(rol="estudiante"))
	#Contar Materias
	mat=mat=len(Materia.objects.all())
	#COntrol
	asis=len(Asistencia.objects.all())
	obs=len(Observacion.objects.all())
	noto=len(Nota.objects.all())
	wik=len(Wiki.objects.all())
	user_active=request.user.rol
	if user_active == 'estudiante':
		return redirect(reverse('front'))
	ctrl=asis+obs
	data={'registro':registro,'est':est,'mat':mat, 'crtl':ctrl,'noto':noto,'wik':wik}
	return render_to_response('index.html',data, context_instance=RequestContext(request))

@login_required(login_url='login')
def front(request):
	user=request.user.rol
	print user
	return render_to_response('front.html',context_instance=RequestContext(request))


def reportes(request):
	return render_to_response('panelControl/Reportes.html',context_instance=RequestContext(request))	

def recursos(request):
	return render_to_response('panelControl/Recursos.html',context_instance=RequestContext(request))


def matriculas(request):
	return render_to_response('panelControl/Matriculas.html',context_instance=RequestContext(request))

def control(request):
	return render_to_response('panelControl/Control.html',context_instance=RequestContext(request))

def configuracion(request):
	return render_to_response('panelControl/Configuracion.html',context_instance=RequestContext(request))


def boletin(request):
	return render_to_response('crud/Boletines.html',context_instance=RequestContext(request))

def crearBoletin(request):
	return render_to_response('forms/FcrearBoletines.html',context_instance=RequestContext(request))

def buscarBoletin(request):
	return render_to_response('forms/FbuscarBoletines.html',context_instance=RequestContext(request))

def usoPlataforma(request):
	return render_to_response('crud/UsoDePlataforma.html', context_instance=RequestContext(request))

def buscarEstadistica(request):
	return render_to_response('forms/FbuscarUsoDePlataforma.html', context_instance=RequestContext(request))

def logros(request):
	return redirect(reverse('logro'),context_instance=RequestContext(request))

def actividades(request):
	return redirect(reverse('actividad'),context_instance=RequestContext(request))

def indicadores(request):
	return redirect(reverse('indicador'),context_instance=RequestContext(request))

def asistencia(request):
	return redirect(reverse('selMat'),context_instance=RequestContext(request))

def observador(request):
	return redirect(reverse('selObs'),context_instance=RequestContext(request))

def herramienta(request):
	return redirect(reverse('crudHerramientas'),context_instance=RequestContext(request))

def api(request):
	return redirect(reverse('Api'),context_instance=RequestContext(request))

