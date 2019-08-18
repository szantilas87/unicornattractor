from django.test import SimpleTestCase
from django.urls import reverse, resolve
from contacts.views import contact, newsletter

class TestContactsUrls(SimpleTestCase):

    def test_contact_url_resolves(self):
        url = reverse('contact')
        self.assertAlmostEquals(resolve(url).func, contact)

    def test_newsletter_url_resolves(self):
        url = reverse('newsletter')
        self.assertAlmostEquals(resolve(url).func, newsletter)