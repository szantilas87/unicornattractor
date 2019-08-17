from django.test import SimpleTestCase
from bugs.forms import FilterView

class TestBugsForms(SimpleTestCase):

    def test_sort_form_valid_data(self):
        form = FilterView(data={
            'order_by': 'name_az'
        })
        
        self.assertTrue(form.is_valid())

    def test_sort_form_no_data(self):
        form = FilterView(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)