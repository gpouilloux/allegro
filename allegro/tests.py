from django.test import TestCase, Client
from django.core.urlresolvers import reverse

# Create your tests here.


class SimpleTest(TestCase):

    def test_helloworld(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)