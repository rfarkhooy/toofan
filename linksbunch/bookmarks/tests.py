"""All tests related to Bookmarks application goes here"""
import httplib

from django.test import TestCase


class BookmarksViews(TestCase):
    """Tests all views in Bookmarks application"""

    def test_views(self):
        """Tests all views to see whether all have the response 200 response
           code"""
        response = self.client.get('/bookmarks/')
        self.assertEqual(response.status_code, httplib.OK)
