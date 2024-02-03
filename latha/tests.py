"""
    Class description: This is a test class for the latha module.
"""
from django.test import TestCase
from django.urls import reverse
class HelloWorldViewTest(TestCase):
    """
    Class description: This is a test class for the latha module.
    """
    def test_hello_world_view(self):
        """
        Function description: This is a test function within the unit TestClass.
        """
        url = reverse('hello_world')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")

class HelloWorldIntegrationTest(TestCase):
    """
    Class description: This is a test class for the latha module.
    """
    def test_hello_world_url(self):
        """
        Functino description: This is a test function within the unit TestClass.
        """
        url = reverse('hello_world')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")
