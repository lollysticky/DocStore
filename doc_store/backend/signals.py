import os

from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Document


@receiver(post_delete, sender=Document)
def delete_file(sender, instance, **kwargs):
    """
    Whenever a Document object is deleted, this action makes sure the associated file gets deleted.
    """
    if os.path.isfile(instance.file.path):
        print("Deleted Document {0}: {1}".format(instance.pk, instance.file.path))
        instance.file.delete(False)
    else:
        print("File {0} not found. Can't delete!".format(instance.file.path))
