from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$','control.views.control', name='control'),
	url(r'^/selCurFal$','control.views.selMat', name='selMat'),
	url(r'^/selMatFal$','control.views.selMat2', name='selMat2'),
	url(r'^/selMatAlu$','control.views.selAlu', name='selAlu'),
	url(r'^/saveAlu$','control.views.saveAlu', name='saveAlu'),
	url(r'^/selCurObs$','control.views.selObs', name='selObs'),
	url(r'^/selMatObs$','control.views.selObs2', name='selobs'),
	url(r'^/selObsUser$','control.views.selObsUser', name='selObsUser'),
	url(r'^/saveObsUser$','control.views.saveObsUser', name='saveObsUser'),






)
