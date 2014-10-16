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
from django.contrib.auth.models import User
from django.db import models
from register.models import Cursos
from pensum.models import *
from custom.models import *
# Create your views here.

#Registro de usuarios
def herramientas(request):
	
	data = {}
	if request.session.get('message'):
		data = {'message': request.session['message']}
		del request.session['message']

	return render_to_response('panelControl/Recursos.html',data, context_instance=RequestContext(request))

def crudHerramientas(request):
	return render_to_response('crud/Herramienta.html',context_instance=RequestContext(request))

def selCursoWiki(request):
	cursos=Cursos.objects.filter(estado_curso =1)
	data={'cursos':cursos}
	return render_to_response('search/selCurseWiki.html',data,context_instance=RequestContext(request))

def selMatWiki(request):
	uid=request.POST.get("uid")
	materias=Materia.objects.filter(id_cursos =uid)
	data={'materias':materias}
	return render_to_response('search/selCurseMatWiki.html',data,context_instance=RequestContext(request))

def formWiki(request):
	uid=request.POST.get("uid")
	materias=Materia.objects.get(id=uid)
	data={'materias':materias}
	return render_to_response('forms/FcrearWiki.html',data,context_instance=RequestContext(request))

def saveWiki(request):
	uid=request.POST.get("uid")
	materias=Materia.objects.get(id=uid)
	id_user=request.user.id
	docente=User.objects.get(id=id_user)
	descripcion=request.POST.get('editor1')
	wiki=Wiki.objects.create(descripcion=descripcion,id_materia=materias,id_docente=docente)
	wiki.save()
	return redirect(reverse('herramientas'),context_instance=RequestContext(request))


def Api(request):
	return render_to_response('crud/API.html',context_instance=RequestContext(request))

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

def boletin(request):
	return redirect(reverse('boletin'),context_instance=RequestContext(request))

def plataforma(request):
	return redirect(reverse('usoPlataforma'),context_instance=RequestContext(request))