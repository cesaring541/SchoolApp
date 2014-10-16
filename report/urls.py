from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$','report.views.report', name='report'),
	url(r'^/repCur$', 'report.views.repCur', name='repCur'),
	url(r'^/repCurMar$', 'report.views.repCurMar', name='repCurMar'),
	url(r'^/repCurMarLog$', 'report.views.repCurMarLog', name='repCurMarLog'),
	url(r'^/repCurMarLogAct$', 'report.views.repCurMarLogAct', name='repCurMarLogAct'),
	url(r'^/notInterna$', 'report.views.notInterna', name='notInterna'),
	url(r'^/notExterna$', 'report.views.notExterna', name='notExterna'),

	url(r'^/notInternaSave$', 'report.views.notInternaSave', name='notInternaSave'),

	
	url(r'^/buscarlogro$','pensum.views.buscarlogro', name='buscarlogro'),
	url(r'^/buscarActividad$','pensum.views.buscarActividad', name='buscarActividad'),
	url(r'^/buscarIndicador$','pensum.views.buscarIndicador', name='buscarIndicador'),
	
	url(r'^/asistencia$','pensum.views.asistencia', name='asistencia'),
	url(r'^/observador$','pensum.views.observador', name='observador'),
	url(r'^/herramienta$','pensum.views.herramienta', name='herramienta'),
	url(r'^/api$','pensum.views.api', name='api'),
	url(r'^/boletin$','pensum.views.boletin', name='boletin'),
	url(r'^/plataforma$','pensum.views.plataforma', name='plataforma'),

)