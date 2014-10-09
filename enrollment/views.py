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
def matriculas(request):
	est=len(User.objects.filter(rol="estudiante"))
	data={'est':est}
	return render_to_response('panelControl/Matriculas.html', data,context_instance=RequestContext(request))

def formEstudiante(request):
	return render_to_response('forms/FcrearEstudiante.html', context_instance=RequestContext(request))

def createMatricular(request):
	first_name=request.POST.get('firstname')
	last_name=request.POST.get('lastname')
	grado=request.POST.get('grado')
	username = first_name+"."+last_name
	password = request.POST.get('documento')
	email=request.POST.get('email')
	usuario = User.objects.create_user(username=username,email=email,password=password)
	usuario.first_name=request.POST.get('firstname')
	usuario.last_name=request.POST.get('lastname')
	usuario.rol="estudiante"
	usuario.grado=request.POST.get('grado')

	usuario.avatar=request.FILES.get('avatar') if request.FILES.get('avatar') else 'images/avatars/avatar.png'
	usuario.save()
	############################################################
	datosPersonales=InfoBasica.objects.create(id_user=usuario)
	datosPersonales.fecha_nacimiento=request.POST.get('fecha_nacimiento')
	datosPersonales.celular=request.POST.get('celularEst')
	datosPersonales.eps=request.POST.get('eps')
	datosPersonales.tipo_sangre=request.POST.get('tipo_sangre')
	datosPersonales.cedula=request.POST.get('documento')
	datosPersonales.observaciones=request.POST.get('observacion')
	datosPersonales.posibles_alergias=request.POST.get('posibles_alergias')
	datosPersonales.save()
	############################################################
	first_name_acudiente=request.POST.get('firts-acudiente')
	last_name_acudiente=request.POST.get('firtslast-acudiente')
	username_acuediente = "acudiente."+first_name_acudiente+"."+last_name_acudiente
	try:
		padre=User.objects.get(username=username_acuediente)

		try:
			nucleoExiste=NucleoFamliar.objects.get(id_user=usuario,id_padre=padre)
		
		except NucleoFamliar.DoesNotExist:
			nucleo=NucleoFamliar.objects.create(id_user=usuario,id_padre=padre)
			nucleo.save()

	except User.DoesNotExist:
		padre=None
	if padre is None:
		password_acuediente = request.POST.get('documento2')
		email_acuediente=request.POST.get('emailacud')
		usuario2 = User.objects.create_user(username=username_acuediente,email=email_acuediente,password=password_acuediente)
		usuario2.first_name=request.POST.get('firstname')
		usuario2.last_name=request.POST.get('lastname')
		usuario2.rol="acudiente"
		usuario2.avatar=request.FILES.get('avatar') if request.FILES.get('avatar') else 'images/avatars/avatar.png'
		usuario2.save()
		celular_padre=request.POST.get('celular')
		celular_padre2=request.POST.get('celular2')
		###############################################
		profesion=request.POST.get('profesion')
		direccion=request.POST.get('direccion')
		infoBasica=InfoFamiliar.objects.create(id_padre=usuario2,celular=celular_padre,celular2=celular_padre2,profesion=profesion,direccion=direccion)
		infoBasica.save()
		nucleo=NucleoFamliar.objects.create(id_user=usuario,id_padre=usuario2)
		nucleo.save()
	messages="El estudiante fue matriculado satisfactorioamente"
	data={'messages':messages}
	return render_to_response('panelControl/Matriculas.html',data,context_instance=RequestContext(request))

def SelCurse2(request):
	search=request.POST.get('search')
	cursos=Cursos.objects.filter(nombre_curso__contains =search)
	data={'cursos':cursos}
	return render_to_response('search/selCurEst.html',data,context_instance=RequestContext(request))

def SelCurse(request):
	search=request.POST.get('search')
	cursos=Cursos.objects.filter(nombre_curso__contains ="")
	return render_to_response('search/selCurEst.html',context_instance=RequestContext(request))

def SelCurEst(request):
	uid=request.POST.get('uid')
	curso=Cursos.objects.get(id=uid)
	grado=curso.nombre_curso
	usuarios=User.objects.filter(grado=grado)
	print usuarios
	data={'usuarios':usuarios}

	return render_to_response('search/selEst.html',data,context_instance=RequestContext(request))