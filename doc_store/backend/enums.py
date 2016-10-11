class DOCUMENT_TYPES:

    UNKNOWN = 0
    PDF = 1
    DOCX = 2
    IMG = 3

    CHOICES = [
        (UNKNOWN, 'unknown'),
        (PDF, 'pdf'),
        (DOCX, 'docx'),
        (IMG, 'img')
    ]

    CHOICES_DICT = dict(CHOICES)
