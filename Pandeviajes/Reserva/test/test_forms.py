from django.test import TestCase
from Reserva.models import Reserva


class TestForms(TestCase):
    def TestFormsValid(self):
        R=Reserva.objects.create(nombres='Pepe',apep='Pupu',apem='Papa',
        rut='135226458',edad='18',cantP='2',telef='978704567')
        data={'nombres':R.nombres,'apep':R.apep,'apem':R.apem,
        'rut':R.rut,'edad':R.edad,'cantP':R.cantP,'telef':R.telef,}
        form= Reserva(data=data)
        self.assertTrue(form.is_valid())

    def TestFormsInvalid(self):
        R=Reserva.objects.create(nombres='',apep='Pupu',apem='Papa',
        rut='1352',edad='18',cantP='2',telef='978704567')
        data={'nombres':R.nombres,'apep':R.apep,'apem':R.apem,
        'rut':R.rut,'edad':R.edad,'cantP':R.cantP,'telef':R.telef,}
        form= Reserva(data=data)
        self.assertFalse(form.is_valid())
