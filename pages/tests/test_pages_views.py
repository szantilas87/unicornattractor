from django.test import TestCase, Client
from django.urls import reverse
from pages.models import Query, Comment
from django.test import RequestFactory
from django.contrib.auth.models import User
from mixer.backend.django import mixer
from pages.views import query_detail



class TestPagesViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_GET(self):
        self.home_url = reverse('home')
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

    def test_particular_user_GET(self):
        mixer.blend(User, username='apple')
        self.user_detail_url = reverse('user-queries', args=['apple'])
        response = self.client.get(self.user_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/user_queries.html')

    def test_particular_query_detail_GET(self):
        mixer.blend('pages.Query')
        self.query_detail_url = reverse('query-detail', kwargs={"id": 1})
        response = self.client.get(self.query_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/query_detail.html')

    def test_update_query_requires_login(self):
        mixer.blend('pages.Query')
        self.query_detail_url = reverse('query-update', kwargs={"pk": 1})
        response = self.client.post(self.query_detail_url, {
                                    'title': 'randomtitle', 'content': 'randomcontent'})

        self.assertEqual(response.status_code, 302)
        self.assertEquals(response.url, '/login/?next=/query/1/update')

    def test_delete_query_requires_login(self):
        mixer.blend('pages.Query')
        self.query_detail_url = reverse('query-delete', kwargs={"pk": 1})
        response = self.client.post(self.query_detail_url, {})

        self.assertEqual(response.status_code, 302)
        self.assertEquals(response.url, '/login/?next=/query/1/delete')

    def test_about_GET(self):
        self.about_url = reverse('about')
        response = self.client.get(self.about_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')

    def test_search_GET(self):
        self.search_url = reverse('search')
        response = self.client.get(self.search_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/search.html')


