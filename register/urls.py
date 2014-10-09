from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$','register.views.registro', name='registro'),
	url(r'^/usuarios$','register.views.usuario', name='usuarios'),
	url(r'^/cursos$','register.views.cursos', name='cursos'),
	url(r'^/formUsuario$','register.views.formUsuario', name='formUsuario'),
	url(r'^/formCurso$','register.views.formCurso', name='formCurso'),
	url(r'^/add_user$','register.views.add_user', name='add_user'),
	url(r'^/search$','register.views.search', name='search'),
	url(r'^/searchUser$','register.views.searchUser', name='searchUser'),
	url(r'^/editar/(?P<id>\d+)$', 'register.views.edit_user', name='edit_user'),
	url(r'^/editar/update_user$', 'register.views.update_user', name='update_user'),
	url(r'^/searchDoc','register.views.searchDoc', name='searchDoc'),
	url(r'^/selDoc/(?P<id>\d+)$', 'register.views.selDoc', name='selDoc'),
	url(r'^/add_curso$','register.views.add_curso', name='add_curso'),
	url(r'^/searchCurse$','register.views.searchCurse', name='searchCurse'),
	url(r'^/selCurse$','register.views.selCurse', name='selCurse'),
	url(r'^/selCurse2$','register.views.selCurse2', name='selCurse2'),
	url(r'^/updateCurse$','register.views.updateCurse', name='updateCurse'),






)
