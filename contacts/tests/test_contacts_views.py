from django.test import TestCase, Client
from django.urls import reverse
from contacts.models import Contact
from datetime import datetime

class TestContactsViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_contact_create_POST(self):
        contacts_count = Contact.objects.count()
        url = reverse('contact')
        response = self.client.post(url, {
            'name': "randomname",
            'email': "randomtext@randomtext.com",
            'message': "randomtext",
            'user_id': 1,
            'contact_date': datetime.now
        })
        contact = Contact.objects.get(id=1)
        self.assertEquals(contact.name, 'randomname')
        self.assertEquals(response.status_code, 302)
        self.assertEqual(Contact.objects.count(), contacts_count+1)
        self.assertEquals(response.url, '/')
        
    def test_newsletter_create_POST(self):
        newsletter_count = Contact.objects.count()
        url = reverse('contact')
        response = self.client.post(url, {
            'name': "randomname2",
            'email': "randomtext2@randomtext.com",
            'message': "randomtext2",
            'user_id': 1,
            'contact_date': datetime.now
        })
        newsletter = Contact.objects.get(id=1)
        self.assertEquals(newsletter.name, 'randomname2')
        self.assertEquals(response.status_code, 302)
        self.assertEqual(Contact.objects.count(), newsletter_count+1)
        self.assertEquals(response.url, '/')