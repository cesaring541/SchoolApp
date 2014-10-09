from django.contrib.auth.models import User
from django.db import models
from register.models import Cursos


class InfoBasica(models.Model):
    id_user = models.ForeignKey(User, db_column='ID_USER')
    fecha_nacimiento = models.CharField(max_length=600, db_column='FECHA_NACIMIENTO') # Field name made lowercase.
    celular = models.CharField(max_length=12, db_column='CELULAR')
    eps = models.CharField(max_length=100, db_column='EPS')
    tipo_sangre = models.CharField(max_length=10, db_column='TIPO_SANGRE') # Field name made lowercase.
    posibles_alergias = models.CharField(max_length=600, db_column='POSIBLES_ALERGIAS') # Field name made lowercase.
    observaciones = models.CharField(max_length=600, db_column='OBSERVACION') # Field name made lowercase.
    cedula = models.CharField(max_length=600, db_column='DOCUMENTO') # Field name made lowercase.


    
    class Meta:
        db_table = u'InfoBasica'

class NucleoFamliar(models.Model):
    id_user = models.ForeignKey(User, db_column='ID_USER')
    id_padre = models.ForeignKey(User, db_column='ID_PADRE',related_name='id acudiente')
    
    
    class Meta:
        db_table = u'NucleoFamiliar'

class InfoFamiliar(models.Model):
    id_padre = models.ForeignKey(User, db_column='ID_PADRE')
    celular = models.CharField(max_length=12, db_column='CELULAR')
    celular2 = models.CharField(max_length=12, db_column='CELULAR2')
    profesion = models.CharField(max_length=100, db_column='PROFESION')
    direccion = models.CharField(max_length=90, db_column='DIRECCION') # Field name made lowercase.
    
    class Meta:
        db_table = u'InfoFamiliar'
