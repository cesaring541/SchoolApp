from django.contrib.auth.models import User
from django.db import models
from register.models import Cursos
from filebrowser.fields import FileBrowseField



class Materia(models.Model):
    id_cursos = models.ForeignKey(Cursos, db_column='ID_CURSOS') # Field name made lowercase.
    id_docente = models.ForeignKey(User, db_column='ID_USER')
    nombre_materia = models.CharField(max_length=600, db_column='NOMBRE_MATERIA') # Field name made lowercase.
    fecha_inicio = models.DateField(db_column='FECHA_INICIO') # Field name made lowercase.
    estado_materia = models.BooleanField(default=True, db_column='ESTADO_MATERIA')
    descripcion_materia = models.CharField(max_length=600, db_column='DESCRIPCION_MATERIA')

    
    class Meta:
        db_table = u'Materia'

class Logro(models.Model):
    id_materia = models.ForeignKey(Materia, db_column='ID_MATERIA') # Field name made lowercase.
    nombre_logro = models.CharField(max_length=600, db_column='NOMBRE_LOGRO') # Field name made lowercase.
    descripcion_logro = models.CharField(max_length=600, db_column='DESCRIPCION') # Field name made lowercase.
    


    
    class Meta:
        db_table = u'Logro'

class Actividad(models.Model):
    id_logro = models.ForeignKey(Logro, db_column='ID_LOGRO') # Field name made lowercase.
    nombre_actividad = models.CharField(max_length=600, db_column='NOMBRE_ACTIVIDAD') # Field name made lowercase.
    descripcion_actividad = models.CharField(max_length=3000, db_column='DESCRIPCION_ACTIVIDAD') # Field name made lowercase.
    fecha_inicio = models.DateField(db_column='FECHA_INICIO')
    fecha_fin = models.DateField(db_column='FECHA_FIN')
    estado_envio=models.BooleanField(default=True, db_column='ESTADO_ENVIO')


    class Meta:
        db_table = u'Actividad'

class Indicador(models.Model):
    id_actividad = models.ForeignKey(Actividad, db_column='ID_ACTIVIDAD') # Field name made lowercase.
    nombre_indicador = models.CharField(max_length=600, db_column='NOMBRE_INDICADOR') # Field name made lowercase.
    descripcion_indicador = models.CharField(max_length=600, db_column='DESCRIPCION_INDICADOR') # Field name made lowercase.
    

    
    class Meta:
        db_table = u'Indicador'

class Nota(models.Model):
    id_actividad = models.ForeignKey(Actividad, db_column='ID_ACTIVIDAD') # Field name made lowercase.
    nota=models.DecimalField(max_digits=3,decimal_places=2,db_column='NOTA')
    id_estudiante = models.ForeignKey(User, db_column='ID_ESTUDIANTE')
    descripcion = models.CharField(max_length=600, db_column='DESCRIPCION_NOTA') # Field name made lowercase.



    class Meta:
        db_table= u'Nota'


        

