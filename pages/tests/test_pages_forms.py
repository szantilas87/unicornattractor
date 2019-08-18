from django.test import SimpleTestCase
from pages.forms import CommentForm

class TestPagesForms(SimpleTestCase):

    def test_commment_form_valid_data(self):
        form = CommentForm(data={
            'content': 'randomtext'
        })

        self.assertTrue(form.is_valid())
    
    def test_comment_form_no_data(self):
        form = CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)