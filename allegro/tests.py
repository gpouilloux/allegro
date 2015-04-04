from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from allegro.models import Document


class SimpleTest(TestCase):
    def test_helloworld(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_adddoc(self):
        docname = 'toto.png'
        newdoc = Document(docfile=docname)
        newdoc.save()
        doc = Document.objects.get(docfile=docname)
        self.assertEqual(doc.docfile, docname)

    def test_listget(self):
        client = Client()
        response = client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)

    def test_listpost(self):
        client = Client()
        docname = 'toto.txt'
        docfile = SimpleUploadedFile(docname, "file_content", content_type="text/plain")
        response = client.post(reverse('list'), {'docfile': docfile})
        self.assertEqual(response.status_code, 302)  # HTTP 302 FOUND
        queryset = Document.objects.get(pk=1)
        self.assertIsNotNone(queryset.id)

    def test_listpostfail(self):
        try:
            Document.objects.get(pk=1)
            self.fail('document does not exist')
        except Document.DoesNotExist:
            pass