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
from django.contrib.auth import hashers
import logging
from models import *
from pensum.models import *
from register.models import *
from front.models import *

#reporte
def report(request):
	data={}
	if request.session.get('message'):
		data = {'message': request.session['message']}
		del request.session['message']
	
	return render_to_response('panelControl/Reportes.html',data, context_instance=RequestContext(request))

def repCur(request):
	cursos=Cursos.objects.filter(estado_curso =1)
	data={'cursos':cursos}
	return render_to_response('search/notCurse.html',data,context_instance=RequestContext(request))

def repCurMar(request):
	uid=request.POST.get("uid")
	materias=Materia.objects.filter(id_cursos =uid)

	data={'materias':materias}
	return render_to_response('search/notCurseMat.html',data,context_instance=RequestContext(request))

def repCurMarLog(request):
	uid=request.POST.get("uid")
	logro=Logro.objects.filter(id_materia =uid)
	user=request.user.id
	
	data={'logro':logro}
	return render_to_response('search/notCurseMatLog.html',data,context_instance=RequestContext(request))

def repCurMarLogAct(request):
	uid=request.POST.get("uid")

	actividad=Actividad.objects.filter(id_logro =uid)
	data={'actividad':actividad}
	return render_to_response('search/notCurseMatLogAct.html',data,context_instance=RequestContext(request))

def notInterna(request):
	if 'uid' in request.POST:
		log=request.POST.get('uid')
	else:
		log=request.session.get('uid')
		del request.session['uid']
	uid=request.POST.get("uid")
	actividad=Actividad.objects.get(id =uid,actividad_externa=False)
	nota =Nota.objects.filter(id_actividad=actividad)
	data={'nota':nota,'calificacion':calificacion}
	return render_to_response('search/notExt.html',data,context_instance=RequestContext(request))

def notExterna(request):
	if 'uid' in request.POST:
		uid=request.POST.get('uid')
	else:
		uid=request.session.get('uid')
	actividad=Actividad.objects.get(id =uid,actividad_externa=True)
	nota=Nota.objects.filter(id_actividad=actividad)
	
	request.session['uid']=uid
	data={'nota':nota}
	return render_to_response('search/notExt.html',data,context_instance=RequestContext(request))

def notInternaSave(request):
	uid=request.POST.get("ui-not")
	nota=request.POST.get("nota")
	envio=Envio.objects.get(id=uid)
	estud=envio.id_estudiante_id
	actividad=envio.id_actividad_id
	act=Actividad.objects.get(id=actividad)
	estudiante=User.objects.get(id=estud)
	nota=Nota.objects.create(id_actividad=act,id_estudiante=estudiante,nota=nota)

	return redirect(reverse('notInterna'))

def buscarlogro(request):
	return render_to_response('edit/FbuscarLogro.html',context_instance=RequestContext(request))

def buscarActividad(request):
	return render_to_response('edit/FbuscarActividad.html',context_instance=RequestContext(request))

def buscarIndicador(request):
	return render_to_response('edit/FbuscarIndicador.html',context_instance=RequestContext(request))	

def asistencia(request):
	return redirect(reverse('selMat'),context_instance=RequestContext(request))

def observador(request):
	return redirect(reverse('selObs'),context_instance=RequestContext(request))

def herramienta(request):
	return redirect(reverse('crudHerramientas'),context_instance=RequestContext(request))

def api(request):
	return redirect(reverse('herramientas'),context_instance=RequestContext(request))

def boletin(request):
	return redirect(reverse('boletin'),context_instance=RequestContext(request))

def plataforma(request):
	return redirect(reverse('usoPlataforma'),context_instance=RequestContext(request))
