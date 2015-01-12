from django.db import models

# Create your models here.

class Jornada ( models.Model ):
	nombre = models.CharField( max_length=64 )
	fechadejuego = models.DateField( null=True )

	def __unicode__ ( self ):
		return self.nombre

class Partido ( models.Model ):
	numero = models.IntegerField( )
	local = models.CharField( max_length=64 )
	visitante = models.CharField( max_length=64 )
	is_pleno = models.BooleanField( default = False )

	jornada = models.ForeignKey ( Jornada )

	def __unicode__ ( self ):
		return self.jornada.nombre + " - " + str(self.numero) + ". " + self.local + " - " + self.visitante

