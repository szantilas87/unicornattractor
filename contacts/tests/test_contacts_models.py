from django.test import TestCase
from contacts.models import Contact
from mixer.backend.django import mixer

class TestContactsModels(TestCase):

    def test_contact_creation(self):
        contact = mixer.blend('contacts.Contact')
        self.assertTrue(isinstance(contact, Contact))
        self.assertEqual(str(contact), contact.name)
       