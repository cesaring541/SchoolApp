from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = patterns('',
	url(r'^back/', include('admin.urls')),
	url(r'^plataform/', include('front.urls')),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)