from django.test import TestCase, Client
from django.urls import reverse

class TestBugsViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.bugs_url = reverse('bugs')
    
    def test_bugs_GET(self):
        response = self.client.get(self.bugs_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bugs/bug_queries.html')

    def test_new_bug_create_requires_login(self):
        url = reverse('bug-create')
        response = self.client.post(url, {
            'title': 'project2',
            'content': 'design'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/login/?next=/query/new-bug')