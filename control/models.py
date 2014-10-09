from django.contrib.auth.models import User
from django.db import models
from register.models import Cursos
from pensum.models import *


class Asistencia(models.Model):
    id_materia = models.ForeignKey(Materia, db_column='ID_MATERIA') # Field name made lowercase.
    id_estudiante = models.ForeignKey(User, db_column='ID_ESTUDIANTE')
    fecha_falla = models.DateField(db_column='FECHA_FALLA') # Field name made lowercase.
    descripcion_falla = models.CharField(max_length=600, db_column='DESCRIPCION_FALLA')
  

    
    class Meta:
        db_table = u'Asistencia'

class Observacion(models.Model):
    id_estudiante = models.ForeignKey(User, db_column='ID_ESTUDIANTE')
    fecha_falla = models.DateField(db_column='FECHA_FALLA') # Field name made lowercase.
    descripcion_falla = models.CharField(max_length=600, db_column='DESCRIPCION_FALLA')
    tipo = models.CharField(max_length=600, db_column='TIPO')
    id_docente = models.ForeignKey(User, db_column='ID_DOCENTE',related_name='id_docente')


    
    class Meta:
        db_table = u'Observacion'