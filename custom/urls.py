from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^/$','custom.views.herramientas', name='herramientas'),
	url(r'^/crudHerr$','custom.views.crudHerramientas', name='crudHerramientas'),
	url(r'^/selCursoWiki$','custom.views.selCursoWiki', name='selCursoWiki'),
	url(r'^/selMatWiki$','custom.views.selMatWiki', name='selMatWiki'),	
	url(r'^/formWiki$','custom.views.formWiki', name='formWiki'),	
	url(r'^/saveWiki$','custom.views.saveWiki', name='saveWiki'),	

)
