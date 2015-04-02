from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from allegro.forms import DocumentForm
from allegro.models import Document


def index(request):
    return render(request, 'allegro/index.html')

def list(request):

    """
    # Handle file upload
    :param request: HTTP request
    :return: list page with the documents and the form
    """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('allegro.views.list'))
    else:
        form = DocumentForm()

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'allegro/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )