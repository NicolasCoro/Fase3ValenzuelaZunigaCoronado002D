from django.db import models
from django.urls import reverse

# Create your models here.

class Reserva(models.Model):
	nombres=models.CharField(max_length=60)
	apep=models.CharField(max_length=20)
	apem=models.CharField(max_length=20)
	rut=models.CharField(max_length=9)
	edad=models.IntegerField(default=0)
	cantP=models.IntegerField(default=0)
	telef=models.IntegerField(default=0)
	SEL_DEST = (
		('NA', 'Selecciona un destino'),
		('HAWAI', 'Hawai'),
		('PARIS', 'Paris'),
		('MOSCY', 'Moscu'),
		('TOKIO', 'Tokio'),
		('SHANGAI', 'Shangai'),
		('BERLIN', 'Berlin'),
		('DUBAI', 'Dubai'),
	)

	destinos = models.CharField(
		max_length=21,
		choices=SEL_DEST,
		blank=True,
		default='NA',
		help_text='Destinos',
	)
    
	
	def _str_(self):
		return self.nombre	

	
	def get_absolute_url(self):
		return reverse('reserva_detail', args=[str(self.id)])