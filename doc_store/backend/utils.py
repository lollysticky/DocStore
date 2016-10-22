import hashlib

from .models import Document, Project


def save_documents(uploaded_files, project_uuid):
    """
    Save documents to the database
    """
    if project_uuid:
        project = Project.objects.get(id=project_uuid)
    else:
        project = None

    for uploaded_file in uploaded_files:
        instance = Document(original_filename=uploaded_file.name,
                            md5=md5(uploaded_file),
                            file=uploaded_file,
                            project=project)
        instance.save()
        print("Save to django storage")


def md5(uploaded_file):
    """
    Calculate md5 key of uploaded file
    """
    md5 = hashlib.md5()
    for chunk in uploaded_file.chunks():
        md5.update(chunk)
    return md5.hexdigest()


def extract_image_from_text(image_file):
    """
    Using a wrapper around Google's Tesseract OCR: https://pypi.python.org/pypi/pytesseract
    wrappers: https://github.com/tesseract-ocr/tesseract/wiki/AddOns#tesseract-wrappers
    """


def get_project_choices(add_empty=True):
    """
    Retrieve all project choices
    :param add_empty: add an 'empty' project; used in the SelectionWidget
    :return: a list of tuples
    """
    choices = []
    for project in Project.objects.all():
        choices.append((str(project.id), project.ref_id))
    if add_empty:
        choices.append(('', '--------'))
    return choices
