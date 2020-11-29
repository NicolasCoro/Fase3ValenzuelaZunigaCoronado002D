from django.test import TestCase
from Reserva.models import Reserva

class ReservaTest(TestCase):
    def setUp(self):
        self.reserva1=Reserva.objects.create(nombres='Nicolas',rut='201234567')

     
    def test(self):
        max_length=Reserva._meta.get_field('nombres').max_length
        self.assertEquals(max_length,60) 

