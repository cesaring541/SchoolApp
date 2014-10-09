from django.contrib.auth.models import User
from django.db import models
from register.models import Cursos
from pensum.models import *

class Wiki(models.Model):
    descripcion = models.CharField(max_length=50, db_column='DESCRIPCION')
    id_docente = models.ForeignKey(User, db_column='ID_USER')
    id_materia = models.ForeignKey(Materia,db_column="ID_MATERIA")

    class Meta:
        db_table = u'Wiki'