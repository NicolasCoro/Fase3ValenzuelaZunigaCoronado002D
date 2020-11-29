from django.test import TestCase
from . models import Reserva, Contacto

class ReservaTestCase(TestCase):
    def setUp(self):
        a1=Reserva.objects.create(rut="206270578")
        a2=Reserva.objects.create(rut="123456789")
        Reserva.objects.create(nombres="Nicolas", Reserva=a1)
       
    
    def test(self):
        reserva1= Reserva.objects.get(rut="206270578")
        self.assertEqual(reserva1.Reserva.nombres,"Nicolas") 

