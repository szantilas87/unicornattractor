from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import QueryListView, QueryUpdateView, QueryDeleteView, UserQueryListView, about, search, like_query, paid, query_detail

class TestPagesUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, QueryListView)

    def test_user_queries_url_resolves(self):
        url = reverse('user-queries', args=['xxx'])
        self.assertEquals(resolve(url).func.view_class, UserQueryListView)
        
    def test_query_update_url_resolves(self):
        url = reverse('query-update', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, QueryUpdateView)

    def test_query_delete_url_resolves(self):
        url = reverse('query-delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, QueryDeleteView)

    def test_about_url_resolves(self):
        url = reverse('query-detail', kwargs={'id': 1})
        self.assertAlmostEquals(resolve(url).func, query_detail)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertAlmostEquals(resolve(url).func, about)

    def test_search_url_resolves(self):
        url = reverse('search')
        self.assertAlmostEquals(resolve(url).func, search)

    def test_paid_url_resolves(self):
        url = reverse('paid')
        self.assertAlmostEquals(resolve(url).func, paid)

    def test_like_query_url_resolves(self):
        url = reverse('like_query')
        self.assertAlmostEquals(resolve(url).func, like_query)

