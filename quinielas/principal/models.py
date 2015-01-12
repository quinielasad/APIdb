from django.db import models
#import User
from django.contrib.auth.models import User
# Create your models here.

class Perfil (models.Model):
	puntuacion = models.IntegerField ( )
	user = models.ForeignKey( User )

	def __unicode__ ( self ):
		return self.user.name

class Jornada ( models.Model ):
	nombre = models.CharField( max_length=64 )
	fechadejuego = models.DateField( null=True )

	def __unicode__ ( self ):
		return self.nombre

class Partido ( models.Model ):
	APUESTA = (
		('0', '0'),
    	('1', '1'),
    	('X', 'X'),
    	('2', '2'),
	)
	APUESTA_GOL = (
    	('0', '0'),
    	('1', '1'),
    	('2', '2'),
    	('M', 'M'),
	)

	#datos genericos del partido
	numero = models.IntegerField( )
	local = models.CharField( max_length=64 )
	visitante = models.CharField( max_length=64 )
	isPleno = models.BooleanField( default = False )

	#apuesta comun
	unoComun = models.DecimalField( default=0.0, decimal_places=2, max_digits=4, blank=True )
	xComun = models.DecimalField( default=0.0, decimal_places=2, max_digits=4, blank=True)
	doscomun = models.DecimalField( default=0.0, decimal_places=2, max_digits=4, blank=True )
	#if isPleno:
	golLocal = models.CharField( choices=APUESTA_GOL, max_length=12, null=True, blank=True)
	golVisitante = models.CharField( choices=APUESTA_GOL, max_length=12, null=True, blank=True )

	#resultados
	resultado = models.CharField ( choices=APUESTA, default="0", max_length=12, blank=True )
	resultadoLocal = models.CharField( choices=APUESTA_GOL, max_length=12, null=True, blank=True )
	resultadoVisitante = models.CharField( choices=APUESTA_GOL, max_length=12, null=True, blank=True )

	#datos foreingkey
	jornada = models.ForeignKey ( Jornada )

	def __unicode__ ( self ):
		return self.jornada.nombre + " - " + str(self.numero) + ". " + self.local + " - " + self.visitante

class ApuestaPartido (models.Model):
	APUESTA = (
    	('1', '1'),
    	('X', 'X'),
    	('2', '2'),
	)

	value = models.CharField ( choices=APUESTA, default="0", max_length=12 )

	#datos foreingkey
	user = models.ForeignKey( User )
	partido = models.ForeignKey( Partido )

	def __unicode__ ( self ):
		return self.user.username + " - " + self.partido.jornada.nombre + "." + str(self.partido.numero) + " = " + self.value
