from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bugs.views import bugs, BugCreateView

class TestBugsUrls(SimpleTestCase):
    def test_bugs_url_resolves(self):
        url = reverse('bugs')
        self.assertEquals(resolve(url).func, bugs)

    def test_create_bug_resolves(self):
        url = reverse('bug-create')
        self.assertEquals(resolve(url).func.view_class, BugCreateView)
    
