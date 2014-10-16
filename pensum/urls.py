from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$','pensum.views.pensum', name='pensum'),
	url(r'^/materias$','pensum.views.materias', name='materias'),
	url(r'^/logro$','pensum.views.logro', name='logro'),
	url(r'^/actividad$','pensum.views.actividad', name='actividad'),
	url(r'^/indicador$','pensum.views.indicador', name='indicador'),
	url(r'^/formMateria$','pensum.views.formMateria', name='formMateria'),
	url(r'^/formMateria2$','pensum.views.formMateria2', name='formMateria2'),
	url(r'^/formActividad$','pensum.views.formActividad', name='formActividad'),
	url(r'^/formIndicador$','pensum.views.formIndicador', name='formIndicador'),
	url(r'^/searchUser$','pensum.views.searchUser', name='searchUser'),
	url(r'^/selMat/(?P<id>\d+)$', 'pensum.views.selMat', name='selMat'),
	url(r'^/add_Materia$','pensum.views.add_Materia', name='add_Materia'),
	url(r'^/selCursoLog$','pensum.views.selCursoLog', name='selCursoLog'),
	url(r'^/selCursoLog1$','pensum.views.selCursoLog1', name='selCursoLog1'),
	url(r'^/selMatLog1$','pensum.views.selMatLog1', name='selMatLog1'),
	url(r'^/createCurso$','pensum.views.createCurso', name='createCurso'),
	url(r'^/LogMenu$','pensum.views.LogMenu', name='LogMenu'),
	url(r'^/selCursoAct$','pensum.views.selCursoAct', name='selCursoAct'),
	url(r'^/selCursoAct1$','pensum.views.selCursoAct1', name='selCursoAct1'),
	url(r'^/selMatAct1$','pensum.views.selMatAct1', name='selMatAct1s'),
	url(r'^/selMatActLog$','pensum.views.selMatActLog', name='selMatActLog'),
	url(r'^/saveAct$','pensum.views.saveAct', name='saveAct'),
	url(r'^/searchSelCursoLog$','pensum.views.searchSelCursoLog', name='searchSelCursoLog'),
	url(r'^/searchSelMatLog1$','pensum.views.searchSelMatLog1', name='searchSelMatLog1'),
	url(r'^/searchSelCursoLog2$','pensum.views.searchSelCursoLog2', name='searchSelCursoLog2'),


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