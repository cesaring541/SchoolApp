from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$','enrollment.views.matriculas', name='matriculas'),
	url(r'^/formEstudiante$','enrollment.views.formEstudiante', name='formEstudiante'),
	url(r'^/createMatricula$','enrollment.views.createMatricular', name='createMatricular'),
	url(r'^/SelCurse$','enrollment.views.SelCurse', name='SelCurse'),
	url(r'^/SelCurse2$','enrollment.views.SelCurse2', name='SelCurse2'),
	url(r'^/SelCurEst$','enrollment.views.SelCurEst', name='SelCurEst'),



)
