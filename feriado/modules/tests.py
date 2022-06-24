from email import message
from http import HTTPStatus
from django.test import TestCase
from .FeriadosAPI import FeriadosAPI
from .forms import FeriadoForm

class FeriadoFormTest(TestCase):
    def test_form_has_fields(self):
        form = FeriadoForm()
        expected = ['nome', 'dia', 'mes', 'ano']
        self.assertSequenceEqual(expected, list(form.fields))
        
    def test_properties(self):
        objeto = FeriadosAPI(2022)
        assert objeto.ano == '2022'
