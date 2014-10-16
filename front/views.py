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
from control.models import *
from custom.models import *


@login_required(login_url='login')
def front(request):
	dat=request.user.grado
	cursos = None
	materias = None

	try:
		cursos=Cursos.objects.get(nombre_curso=dat)
		materias=Materia.objects.filter(id_cursos=cursos.id)
	except Cursos.DoesNotExist:
		pass
	rol=request.user.rol
	print rol+"no"
	if rol != 'estudiante':
		print rol
		return render_to_response('examples/500.html',context_instance=RequestContext(request))

	data={'materias':materias}
	return render_to_response('front/front.html',data,context_instance=RequestContext(request))

def fromMenu(request):
	curso=request.POST.get('uid')
	materia=None
	logros=None
	herramientas=None
	user=None
	estudiante=None
	nota=None
	try:
		materia=Materia.objects.get(id=curso)
		logros=Logro.objects.filter(id_materia=materia)
		log=len(logros)
		herramientas=Wiki.objects.filter(id_materia=materia)
		herr=len(herramientas)
		user=request.user.id
		estudiante=User.objects.get(id=user)
		nota=Nota.objects.filter(id_estudiante=estudiante)
		n= len(nota)

	except Materia.DoesNotExist:
		pass

	data={'curso':curso,'materia':materia,'log':log,'herr':herr,'n':n}
	return render_to_response('front/pages/front/cursos.html', data,context_instance=RequestContext(request))

def fromHerramienta(request):
	mate=request.POST.get('materia')
	materia=Materia.objects.get(id=mate)
	data={'materia':materia}
	return render_to_response('front/pages/front/Herramientas.html',data, context_instance=RequestContext(request))

def fromNotas(request):
	return render_to_response('front/pages/front/Notas.html', context_instance=RequestContext(request))

def Logros(request):
	mate=request.POST.get('materia')
	materia=Materia.objects.get(id=mate)
	logro=Logro.objects.filter(id_materia=materia)
	data={'logro':logro,'materia':materia}
	return render_to_response('front/pages/front/Logros.html', data, context_instance=RequestContext(request))	

def actividades(request):
	if 'logro' in request.POST:
		log=request.POST.get('logro')
	else:
		log=request.session.get('logro')
		del request.session['logro']

	logro=Logro.objects.get(id=log)
	id_user=request.user.id
	usuario=User.objects.get(id=id_user)
	ids=Envio.objects.filter(id_estudiante=usuario).values('id_actividad')
	not_user=Nota.objects.filter(id_estudiante=usuario).values('id_actividad')

	filtered=Actividad.objects.filter(id_logro=logro.id).exclude(id__in=ids)
	try:
		actividad = filtered.exclude(id__in=not_user)
	except Nota.DoesNotExist:
		actividad=filtered
	
		
	data={'actividad':actividad}
	return render_to_response('front/pages/front/Actividades.html', data,context_instance=RequestContext(request))

def saveActividad(request):

	uid=request.POST.get('uid')
	actividad=Actividad.objects.get(id=uid)
	id_user=request.user.id
	usuario=User.objects.get(id=id_user)

	nuevo_envio = Envio.objects.create(id_estudiante=usuario,id_actividad=actividad)


	if request.FILES:
		nuevo_envio.adjunto = request.FILES.get('adjunto')

	nuevo_envio.save()


	request.session['logro']=actividad.id_logro.id

	return redirect(reverse('actividades'))

def foros(request):
	return render_to_response('front/pages/front/Foros.html', data,context_instance=RequestContext(request))

def wikis(request):
	mate=request.POST.get('materia')
	materia=Materia.objects.get(id=mate)
	wiki=Wiki.objects.filter(id_materia=materia)
	data={'wiki':wiki}
	return render_to_response('front/pages/front/Wikis.html', data, context_instance=RequestContext(request))


def observaciones(request):
	est=request.user.id
	obs=Observacion.objects.filter(id_estudiante=est)
	data={'obs':obs}
	return render_to_response('front/pages/front/Observaciones.html', data, context_instance=RequestContext(request))

def paginawiki(request):
	if 'uid' in request.POST:
		uid=request.POST.get('uid')
		print "ERROR"+uid
	else:
		uid=request.session.get('uid')
		del request.session['uid']
	wiki=Wiki.objects.get(id=uid)
	try:
		paginaWikis=PaginaWiki.objects.filter(id_wiki=wiki)
	except PaginaWiki.DoesNotExist:
		paginaWikis=None
	data={'paginaWikis':paginaWikis,'wiki':wiki}
	return render_to_response('front/pages/front/paginawiki.html', data, context_instance=RequestContext(request))

def formPaginaWiki(request):
	uid=request.POST.get("uid")
	wiki=Wiki.objects.get(id=uid)
	data={'wiki':wiki}
	return render_to_response('front/pages/front/CrearPaginaWiki.html',data,context_instance=RequestContext(request))

def saveFormPaginaWiki(request):
	id_wiki=request.POST.get("uid")
	wiki=Wiki.objects.get(id=id_wiki)
	descripcion=request.POST.get('narrativa')
	user_id=request.user.id
	user=User.objects.get(id=user_id)
	paginawiki=PaginaWiki.objects.create(id_wiki=wiki,aporte=descripcion,id_estudiante=user)
	request.session['uid']=id_wiki
	return redirect(reverse('paginawiki'))

def NotaActividad(request):
	user=request.user.id
	estudiante=User.objects.get(id=user)
	nota=request.GET.get('nota')
	uid_act=request.GET.get('uid_act')
	actividad=Actividad.objects.get(id=uid_act)
	nota=Nota.objects.create(id_actividad=actividad,nota=nota,id_estudiante=estudiante)

	code = 'La nota ha sido registrada, <a href="'+reverse('front')+'">Volver a inicio</a>'

	return HttpResponse(code)

def fromNota(request):
	mate=request.POST.get('materia')
	materia=Materia.objects.get(id=mate)
	logros=Logro.objects.filter(id=materia.id)

	all_activities = None
	
	for logro in logros:
		if all_activities:
			all_activities = all_activities + logro.actividad_set.all()
		else:
			all_activities = logro.actividad_set.all()


	

	data={'all_activities':all_activities}
	return render_to_response('front/pages/front/NotaPorMateria.html',data, context_instance=RequestContext(request))
