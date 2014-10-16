from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$','custom.views.herramientas', name='herramientas'),
	url(r'^/crudHerr$','custom.views.crudHerramientas', name='crudHerramientas'),
	url(r'^/selCursoWiki$','custom.views.selCursoWiki', name='selCursoWiki'),
	url(r'^/selMatWiki$','custom.views.selMatWiki', name='selMatWiki'),	
	url(r'^/formWiki$','custom.views.formWiki', name='formWiki'),	
	url(r'^/saveWiki$','custom.views.saveWiki', name='saveWiki'),

	url(r'^/Api$','custom.views.Api', name='Api'),
	url(r'^/logros$','custom.views.logros', name='logros'),
	url(r'^/actividades$','custom.views.actividades', name='actividades'),
	url(r'^/indicadores$','custom.views.indicadores', name='indicadores'),
	url(r'^/asistencia$','custom.views.asistencia', name='asistencia'),
	url(r'^/observador$','custom.views.observador', name='observador'),
	url(r'^/boletin$','custom.views.boletin', name='boletin'),
	url(r'^/plataforma$','custom.views.plataforma', name='plataforma'),

)
