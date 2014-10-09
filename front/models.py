from django.db import models
from django.contrib.auth.models import User
from django.db import models
from register.models import Cursos
from pensum.models import *

class Envio(models.Model):

    def get_upload_path(self, filename):
		url = "files/users/%s/%s" % (self.id_estudiante.id, filename)
		return url


    id_estudiante = models.ForeignKey(User, db_column='ID_ESTUDIANTE')
    id_actividad = models.ForeignKey(Actividad, db_column='ID_ACTIVIDAD') # Field name made lowercase.
    adjunto = models.FileField(upload_to=get_upload_path, blank=True, null=True)



    class Meta:
        db_table=u'Envio'
