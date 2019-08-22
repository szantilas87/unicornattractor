from django.test import SimpleTestCase
from django.urls import reverse, resolve
from features.views import features, FeatureCreateView

class TestFeaturesUrls(SimpleTestCase):
    def test_features_url_resolves(self):
        url = reverse('features')
        self.assertEquals(resolve(url).func, features)

    def test_create_feature_resolves(self):
        url = reverse('feature-create')
        self.assertEquals(resolve(url).func.view_class, FeatureCreateView)
    