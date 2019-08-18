from django.test import TestCase
from pages.models import Query, Comment
from mixer.backend.django import mixer

class TestPagesModels(TestCase):

    def test_query_creation(self):
        query = mixer.blend('pages.Query')
        self.assertTrue(isinstance(query, Query))
        self.assertEqual(str(query), query.title)

    def comment_creation(self):
        comment = mixer.blend('pages.Commet')
        self.assertTrue(isinstance(comment, Comment))
       
        
       