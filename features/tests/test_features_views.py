from django.test import TestCase, Client
from django.urls import reverse


class TestFeaturesViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.features_url = reverse('features')
        self.create_feature_url = reverse('feature-create')
    
    def test_features_GET(self):
        responese = self.client.get(self.features_url)

        self.assertEquals(responese.status_code, 200)
        self.assertTemplateUsed(responese, 'features/features_queries.html')

    def test_new_feature_created_requires_login(self):
        
        responese = self.client.get(self.create_feature_url)
       
        url = reverse('feature-create')
        response = self.client.post(url, {
            'title': 'project2',
            'content': 'design'
        })

        self.assertEquals(responese.status_code, 302)
        self.assertEquals(responese.url, '/login/?next=/query/new-feature/')


