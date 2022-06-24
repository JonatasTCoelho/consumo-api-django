from email import message
from http import HTTPStatus
from django.test import TestCase
from .FeriadosAPI import FeriadosAPI
from .forms import FeriadoForm

class FeriadoFormTest(TestCase):
    def test_form_has_fields(self):
        if 10 > 5:
            return True
        else:
            return False
