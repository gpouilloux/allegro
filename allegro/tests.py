from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

# Create your tests here.
from allegro.models import Document


class SimpleTest(TestCase):

    def test_helloworld(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_adddoc(self):
        docname = 'toto.png'
        newdoc = Document(docfile = docname)
        newdoc.save()
        doc = Document.objects.get(docfile=docname)
        self.assertEqual(doc.docfile, docname)

    def test_list(self):
        client = Client()
        response = client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)