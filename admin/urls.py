from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^$','admin.views.index', name='index'),
	url(r'^login$', 'admin.views.admin_login', name='login'),
	url(r'^logout$', 'admin.views.admin_logout', name='logout'),
	url(r'^registro', include('register.urls')),
	url(r'^matriculas', include('enrollment.urls')),
	url(r'^recursos',include('custom.urls')),
	url(r'^pensum',include('pensum.urls')),
	url(r'^control',include('control.urls')),
	url(r'^configuracion$','admin.views.configuracion', name='configuracion'),

)