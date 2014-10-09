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



#Registro de usuarios
def control(request):
	asis=len(Asistencia.objects.all())
	obs=len(Observacion.objects.all())
	data = {'asis':asis, 'obs':obs}
	if request.session.get('message'):
		data = {'message': request.session['message']}
		del request.session['message']

	return render_to_response('panelControl/Control.html', data, context_instance=RequestContext(request))


def selMat(request):
	cursos=Cursos.objects.all()
	data={'cursos':cursos}
	return render_to_response('search/selCurseFal.html',data,context_instance=RequestContext(request))

def selMat2(request):
	uid=request.POST.get("uid")
	materias=Materia.objects.filter(id_cursos =uid)

	#for materia in materias:
	#	print materia, dir(materia)

	data={'materias':materias}
	return render_to_response('search/selCurseFalMat.html',data,context_instance=RequestContext(request))

def selAlu(request):
	uid=request.POST.get("uid")
	materia=Materia.objects.get(id =uid)
	id_curso=materia.id_cursos.id
	curso=Cursos.objects.get(id=id_curso)
	usuarios=User.objects.filter(rol='estudiante',grado=curso.nombre_curso)
	data={'usuarios':usuarios,'materia':materia}
	return render_to_response('search/selCurseFalUse.html',data,context_instance=RequestContext(request))

def saveAlu(request):
	uidMat=request.POST.get('uidmat')
	materia=Materia.objects.get(id =uidMat)
	uid = request.POST.getlist('uid')
	estado = request.POST.getlist('asistencia')
	observacion = request.POST.getlist('observacion')
	fechas = request.POST.getlist('fecha')
	mylist = []
	for inde,id in enumerate(uid):
		mylist.append(request.POST.get('optionsRadios'+id))
		
	
	for index, id in enumerate(uid):

		if mylist[index] == "No":
			alumno=User.objects.get(id=id)
			fecha = fechas[index]
			descripcion_falla = observacion[index]


			new_asist = Asistencia.objects.create(id_materia=materia,id_estudiante=alumno,fecha_falla=fecha,descripcion_falla=descripcion_falla)
	
			request.session['message'] = 'La asistencia se completo'

	return redirect(reverse('control'))

def selMatObs(request):
	cursos=Cursos.objects.all()
	data={'cursos':cursos}
	return render_to_response('search/selCurseFal.html',data,context_instance=RequestContext(request))

def selObs(request):
	dat=request.user.id
	cursos=Cursos.objects.all()
	data={'cursos':cursos}
	return render_to_response('search/selCurseObs.html',data,context_instance=RequestContext(request))

def selObs2(request):
	uid=request.POST.get("uid")
	curso=Cursos.objects.get(id=uid)
	usuarios=User.objects.filter(rol='estudiante',grado=curso.nombre_curso)
	data={'usuarios':usuarios}
	return render_to_response('search/selCurseObsUse.html',data,context_instance=RequestContext(request))

def selObsUser(request):
	suid=request.POST.get("uid")
	usuarios=User.objects.get(id=suid)
	data={'usuarios':usuarios}
	return render_to_response('forms/FcrearObservacion.html',data,context_instance=RequestContext(request))

def saveObsUser(request):
	suid=request.POST.get("uid")
	fecha=request.POST.get("fecha")
	descripcion=request.POST.get("descripcion")
	tipo=request.POST.get("tipo")
	dat=request.user.id
	estudiante=User.objects.get(id=suid)
	docente=User.objects.get(id=dat)

	observacion=Observacion.objects.create(id_estudiante=estudiante,fecha_falla=fecha,descripcion_falla=descripcion,tipo=tipo,id_docente=docente)
	request.session['message'] = 'La observacion se completo'
		
	return redirect(reverse('control'))
