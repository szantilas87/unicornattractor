from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from pages.models import Query
from pages.views import query_detail
from mixer.backend.django import mixer



class TestBugsViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.bugs_url = reverse('bugs')
        self.create_bug_url = reverse('bug-create')
    
    def test_bugs_GET(self):
        responese = self.client.get(self.bugs_url)

        self.assertEquals(responese.status_code, 200)
        self.assertTemplateUsed(responese, 'bugs/bug_queries.html')

    def test_new_bug_created_requires_login(self):
        
        responese = self.client.get(self.create_bug_url)

       
        url = reverse('bug-create')
        response = self.client.post(url, {
            'title': 'project2',
            'content': 'design'
        })
        
        self.assertEquals(responese.status_code, 302)
        self.assertEquals(responese.url, '/login/?next=/query/new-bug')