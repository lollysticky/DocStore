from django.shortcuts import render, get_object_or_404
from .forms import FileFieldForm
from .utils import save_documents
from .models import Document, Project

# Create your views here.


def test(request):
    context = {'message': "Hello, world. You're at the backend index."}
    return render(request, 'html/test.html', context)


def index(request, messages=None):
    """
    The main overview page
    """
    documents = Document.objects.all()
    projects = Project.objects.all()
    context = {'documents': documents, 'projects': projects}
    if messages:
        context['messages'] = messages
    return render(request, 'html/overview.html', context)


def upload(request):
    """
    Upload view
    """
    # Handle file upload
    if request.method == 'POST':
        form = FileFieldForm(request.POST, request.FILES)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            project = form.cleaned_data['project_field']
            save_documents(files, project)

            # Redirect to upload form
            form = FileFieldForm()
            context = {
                'messages': ['Successfully uploaded {0} files'.format(len(files))],
                'form': form
            }
            return render(request, 'html/upload.html', context)
    else:
        form = FileFieldForm()

    # Load documents for the list page
    # documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request, 'html/upload.html', {'form': form})


def single_document_details(request, id):
    """
    Show the details of a single document
    :param request: the HTTP request
    :param id: the Document object id
    :return: the document detail page
    """
    document = Document.objects.get(id=id)
    return render(request, 'html/detail.html', {'document': document})


def single_document_delete(request, id):
    """
    Delete a single document
    :param request: the HTTP request
    :param id: the Document object id
    :return: the document overview page
    """
    get_object_or_404(Document, pk=id).delete()
    return index(request, messages=['Deleted document with id {0}'.format(id)])
