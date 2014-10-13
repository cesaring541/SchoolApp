from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^$','front.views.front', name='front'),
	url(r'^login$', 'admin.views.admin_login', name='login'),
	url(r'^logout$', 'admin.views.admin_logout', name='logout'),
	url(r'^fromMenu$', 'front.views.fromMenu', name='fromMenu'),
	url(r'^fromHerramienta$', 'front.views.fromHerramienta', name='fromHerramienta'),
	url(r'^fromNotas$', 'front.views.fromNotas', name='fromNotas'),
	url(r'^Logros$', 'front.views.Logros', name='Logros'),
	url(r'^actividades$', 'front.views.actividades', name='actividades'),
	url(r'^saveActividad$', 'front.views.saveActividad', name='saveActividad'),
	url(r'^foros$','front.views.foros',name='foros'),
	url(r'^observaciones$', 'front.views.observaciones', name='observaciones'),
	url(r'^wikis$', 'front.views.wikis', name='wikis'),
	url(r'^paginawiki$', 'front.views.paginawiki', name='paginawiki'),
	url(r'^formPaginaWiki$', 'front.views.formPaginaWiki', name='formPaginaWiki'),
	url(r'^saveFormPaginaWiki$', 'front.views.saveFormPaginaWiki', name='saveFormPaginaWiki'),

)