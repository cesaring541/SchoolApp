from django.contrib.auth.models import User
from django.db import models
from thumbs import ImageWithThumbsField

#Modelo para los usuarios del sitio, este modelo extiende el modelo de usuarios de Django
class SiteUser(User):
	ImageWithThumbsField(upload_to='images/avatars', sizes=((200,200))).contribute_to_class(User,'avatar')
	models.CharField(max_length=100).contribute_to_class(User,'rol')
	models.CharField(max_length=60).contribute_to_class(User,'grado')

class Cursos(models.Model):
    nombre_curso = models.CharField(max_length=600, db_column='NOMBRE_CURSO') # Field name made lowercase.
    fecha_creacion = models.DateField(db_column='FECHA_CREACION') # Field name made lowercase.
    resumen_curso = models.CharField(max_length=600, db_column='RESUMEN_CURSO') # Field name made lowercase.
    estado_curso = models.IntegerField(db_column='ESTADO_CURSO') # Field name made lowercase.

    
    class Meta:
        db_table = u'Cursos'



