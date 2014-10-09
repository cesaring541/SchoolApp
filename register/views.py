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
def registro(request):
	value=len(User.objects.filter(rol=""))
	mat=len(Cursos.objects.all())	
	data = {'value':value,'mat':mat}
	if request.session.get('message'):
		data = {'message': request.session['message']}
		del request.session['message']
	print data
	return render_to_response('panelControl/Registro.html',data, context_instance=RequestContext(request))

def usuario(request):
	value=len(User.objects.filter(rol=""))
	data = {'value':value}
	return render_to_response('crud/Usuarios.html',data, context_instance=RequestContext(request))

def cursos(request):
	mat=len(Cursos.objects.all())
	data = {'mat':mat}
	return render_to_response('crud/Cursos.html',data, context_instance=RequestContext(request))

def formUsuario(request):
	return render_to_response('forms/FcrearUsuario.html', context_instance=RequestContext(request))

def formCurso(request):
	return render_to_response('forms/Fcrearcurso2.html', context_instance=RequestContext(request))


def add_user(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	email=request.POST.get('email')
	country= None
	usuario = User.objects.create_user(username=username,email=email,password=password)
	usuario.first_name=request.POST.get('firstname')
	usuario.last_name=request.POST.get('lastname')
	usuario.avatar=request.FILES.get('avatar') if request.FILES.get('avatar') else 'images/avatars/avatar.png'
	usuario.is_super=request.POST.get('type')
	if usuario.is_super=='Administrador':
		usuario.is_superuser=1
	else:usuario.is_superuser=0
	#ifactive
	if usuario.is_active=='Activo':
		usuario.is_active=1
	else:usuario.is_active=0
	usuario.save()
	request.session['message'] = 'La accion se completo satisfactoriamente'
	return redirect(reverse('registro'))

def search(request):
	return render_to_response('forms/FbuscarUsuario.html',context_instance=RequestContext(request))

def searchUser(request):
	username=request.POST.get('search')
	usuarios=User.objects.filter(username__contains =username,rol="")
	data={'usuarios':usuarios}
	return render_to_response('search/searchUser.html',data,context_instance=RequestContext(request))

def edit_user(request,id):
	usuarios=User.objects.filter(id =id)
	data={'usuarios':usuarios}
	return render_to_response('edit/FcrearUsuario.html',data,context_instance=RequestContext(request))

#Actualiza los datos de un usuario
def update_user(request):
	
    usuario=User.objects.get(id=request.POST.get('uid'))
    passwd=usuario.password
    usuario.password=passwd
    usuario.first_name=request.POST.get('firstname')
    usuario.last_name=request.POST.get('lastname')
    usuario.email=request.POST.get('email')
    usuario.is_super=request.POST.get('type')
    usuario.is_active=request.POST.get('active')
    if usuario.is_super=='Administrador':
    	usuario.is_superuser=1
    else:usuario.is_superuser=0
    if usuario.is_active=='Activo':
    	usuario.is_active=1
    else:usuario.is_active=0
    usuario.save()
    delete_editing_userdata(request)
    return redirect(reverse('registro'))
#elimina los datos del usuario que se estaba editando
def delete_editing_userdata(request):
    try:
        del request.session['uedit']
        del request.session['renderquery']
    except Exception, e:
        logging.exception(e)
    return redirect(reverse('registro'))

#Obtiene listas de usuarios con base a una serie de filtros
def searchDoc(request):
	username=request.POST.get('search')
	usuarios=User.objects.filter(username__contains =username,is_superuser=0)
	data={'usuarios':usuarios}
	return render_to_response('search/selDoc.html',data,context_instance=RequestContext(request))

def selDoc(request,id):
	usuarios=User.objects.filter(id =id)
	data={'usuarios':usuarios}
	return render_to_response('forms/Fcrearcurso2.html',data,context_instance=RequestContext(request))

def add_curso(request):
	nombre_curso=request.POST.get('name_curse')
	id_usuario=request.POST.get('uid')
	fecha_creacion=request.POST.get('date')
	estado_curso=0
	resumen_curso=request.POST.get('resumen_curso')
	estado=request.POST.get('type')
	nuevo_curso=Cursos.objects.create(estado_curso=estado_curso ,fecha_creacion=fecha_creacion,nombre_curso=nombre_curso,resumen_curso=resumen_curso)
	if estado == 'Activo':
		nuevo_curso.estado_curso=1
	else:
		nuevo_curso.estado_curso=0	
	nuevo_curso.save()
	request.session['message'] = 'La accion se completo satisfactoriamente'
	return redirect(reverse('registro'))

def searchCurse(request):
	return render_to_response('forms/FbuscarCurso.html',context_instance=RequestContext(request))

def selCurse(request):
	search=request.POST.get('search')
	cursos=Cursos.objects.filter(nombre_curso__contains =search)
	data={'cursos':cursos}
	return render_to_response('search/selCourse.html',data,context_instance=RequestContext(request))

def selCurse2(request):
	uid=request.POST.get('uid')
	cursos=Cursos.objects.get(id=uid)
	data={'cursos':cursos}

	return render_to_response('forms/FcrearCurso.html',data,context_instance=RequestContext(request))

def updateCurse(request):
	uid=request.POST.get('uid')
	cursos=Cursos.objects.get(id=uid)
	estado=request.POST.get('type')
	cursos.nombre_curso=request.POST.get('name_curse')
	cursos.resumen_curso=request.POST.get('resumen_curso')
	if estado == 'Activo':
		cursos.estado_curso=1
	else:
		cursos.estado_curso=0	
	cursos.save()
	delete_editing_userdata(request)

	request.session['message'] = 'La accion se completo satisfactoriamente'
	return redirect(reverse('registro'))





	


