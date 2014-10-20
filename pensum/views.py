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
from register.models import Cursos
from django.http import HttpResponseRedirect


def pensum(request):
	mat=len(Materia.objects.all())
	log=len(Logro.objects.all())
	act=len(Actividad.objects.all())
	ind=len(Indicador.objects.all())
	data={'mat':mat, 'log':log, 'act':act, 'ind':ind}
	return render_to_response('panelControl/Pensum.html', data,context_instance=RequestContext(request))

def logro(request):
	return render_to_response('crud/Logro.html',context_instance=RequestContext(request))

def materias(request):
	return render_to_response('crud/Materia.html',context_instance=RequestContext(request))

def actividad(request):
	return render_to_response('crud/Actividad.html',context_instance=RequestContext(request))

def indicador(request):
	return render_to_response('crud/Indicador.html',context_instance=RequestContext(request))

def formIndicador(request):
	return render_to_response('forms/FcrearIndicador.html',context_instance=RequestContext(request))

def formMateria(request):
	return render_to_response('forms/FcrearMateria2.html',context_instance=RequestContext(request))

def formMateria2(request):
	data={'cursos':cursos}
	return render_to_response('forms/FcrearMateria.html',data,context_instance=RequestContext(request))

def formActividad(request):
	uid=request.POST.get('uid')
	logro=Logro.objects.get(id=uid)
	data={'logro':logro}
	return render_to_response('forms/FcrearActividad.html',data,context_instance=RequestContext(request))

def createCurso(request):
	uid=request.POST.get('uid')
	cursos=Materia.objects.get(id =uid)
	data={'cursos':cursos}
	return render_to_response('forms/FcrearLogro.html',data,context_instance=RequestContext(request))

def searchUser(request):
	username=request.POST.get('search')
	usuarios=User.objects.filter(username__contains =username,is_superuser=0)
	data={'usuarios':usuarios}
	return render_to_response('search/selCourse2.html',data,context_instance=RequestContext(request))

def selMat(request,id):
	usuarios=User.objects.get(id =id)
	cursos=Cursos.objects.filter(estado_curso =1)
	data={'usuarios':usuarios,'cursos':cursos}
	return render_to_response('forms/FcrearMateria.html',data,context_instance=RequestContext(request))

def add_Materia(request):
	nombre_materia=request.POST.get('nombre_materia')
	id_usuario= request.POST.get('uid')
	usuario = User.objects.get(id=id_usuario)
	id_curso= request.POST.get('curso_seleccionado')
	curso=Cursos.objects.get(nombre_curso=id_curso)
	fecha_inicio=request.POST.get('fecha_inicio')
	descripcion= request.POST.get('resumen_materia')
	nuevo_materia=Materia.objects.create(id_cursos= curso, id_docente= usuario, nombre_materia=nombre_materia, fecha_inicio=fecha_inicio,descripcion_materia= descripcion)
	nuevo_materia.save()

	return redirect(reverse('pensum'),context_instance=RequestContext(request))

def selCursoLog(request):
	return render_to_response('search/selCurselog.html',context_instance=RequestContext(request))

def selCursoLog1(request):
	cursos=Cursos.objects.filter(estado_curso =1)


	data={'cursos':cursos}
	return render_to_response('search/selCurselog.html',data,context_instance=RequestContext(request))

def selMatLog1(request):
	uid=request.POST.get("uid")
	materias=Materia.objects.filter(id_cursos =uid)
	data={'materias':materias}
	return render_to_response('search/selCurseMat.html',data,context_instance=RequestContext(request))

def LogMenu(request):
	menssage='El logro se ha creado satisfactoriamente'
	namelogro=request.POST.get('nameLogro')
	id_materia=request.POST.get("uid")
	materia=Materia.objects.get(id=id_materia)
	logro=Logro.objects.create(nombre_logro=namelogro,id_materia=materia)
	logro.descripcion_logro=request.POST.get("descr")
	logro.save()

	return redirect(reverse('pensum'),context_instance=RequestContext(request))

def selCursoAct(request):
	return render_to_response('search/selCurseAct.html',context_instance=RequestContext(request))

def selCursoAct1(request):
	cursos=Cursos.objects.filter(estado_curso =1)
	data={'cursos':cursos}
	return render_to_response('search/selCurseAct.html',data,context_instance=RequestContext(request))

def selMatAct1(request):
	uid=request.POST.get("uid")
	materias=Materia.objects.filter(id_cursos =uid)
	data={'materias':materias}
	return render_to_response('search/selCurseMatAct.html',data,context_instance=RequestContext(request))

def selMatActLog(request):
	uid=request.POST.get("uid")
	logro=Logro.objects.filter(id_materia =uid)
	data={'logro':logro}
	return render_to_response('search/selCurseMatLogAct.html',data,context_instance=RequestContext(request))

def saveAct(request):
	uid=request.POST.get('uid')
	logro=Logro.objects.get(id=uid)
	nombre_actividad=request.POST.get('nombre')
	fecha_inicio=request.POST.get('fecha_inicio')
	fecha_final=request.POST.get('fecha_final')
	descripcion_actividad=request.POST.get('narrativa')
	is_external = request.POST.get('external')
	print is_external
	is_external = True if is_external == 'on' else False

	if is_external:
		activity_file = request.FILES.get('package')
		actividad=Actividad.objects.create(
		id_logro=logro,nombre_actividad=nombre_actividad,
		fecha_inicio=fecha_inicio,fecha_fin=fecha_final,
		descripcion_actividad=descripcion_actividad,
		actividad_externa=is_external, paquete=activity_file)
	else:
		actividad=Actividad.objects.create(
		id_logro=logro,nombre_actividad=nombre_actividad,
		fecha_inicio=fecha_inicio,fecha_fin=fecha_final,
		descripcion_actividad=descripcion_actividad,
		)
		
	
	#actividad.save()
	return redirect(reverse('pensum'),context_instance=RequestContext(request))

def searchSelCursoLog(request):
	cursos=Cursos.objects.filter(estado_curso =1)
	data={'cursos':cursos}
	return render_to_response('search/searchSelCurselog.html',data,context_instance=RequestContext(request))

def searchSelMatLog1(request):
	uid=request.POST.get("uid")
	materias=Materia.objects.filter(id_cursos =uid)
	data={'materias':materias}
	return render_to_response('search/searchSelCurseMat.html',data,context_instance=RequestContext(request))

def searchSelCursoLog2(request):
	uid=request.POST.get("uid")
	logro=Logro.objects.filter(id_materia =uid)
	data={'logro':logro}
	return render_to_response('search/searchSelCursoLog2.html',data,context_instance=RequestContext(request))


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


	




	




