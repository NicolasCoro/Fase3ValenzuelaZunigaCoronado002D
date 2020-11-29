from django.test import TestCase
from django.urls import reverse


from Reserva.models import Reserva

class TestView(TestCase):
    def TestList(self):
        Rese= Reserva()

        response= Rese.get(reverse('reserva_list'))

        self.assertEquals(response.status_code,200)
        self.assertEquals(response,'templates/Reserva/reserva_list.html')