from django.test import TestCase, Client
from django.urls import reverse


class TestFeaturesViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.features_url = reverse('features')
    
    def test_features_GET(self):
        response = self.client.get(self.features_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'features/features_queries.html')

    def test_new_feature_create_requires_login(self):
        url = reverse('feature-create')
        response = self.client.post(url, {
            'title': 'project2',
            'content': 'design'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/login/?next=/query/new-feature/')


