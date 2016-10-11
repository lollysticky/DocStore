from __future__ import unicode_literals
import uuid

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.postgres.fields import JSONField

from .enums import DOCUMENT_TYPES


class Document(models.Model):
    """
    Any document uploaded to the DocStore
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=12, choices=DOCUMENT_TYPES.CHOICES, default=DOCUMENT_TYPES.UNKNOWN)
    md5 = models.CharField(blank=True, max_length=32)
    original_filename = models.CharField(blank=True, max_length=128)
    project = models.ForeignKey('Project', default=None)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    notes = GenericRelation('Note')
    labels = GenericRelation('Label')

    def __str__(self):
        return "Document: {0}".format(self.original_filename)


class Project(models.Model):
    """
    A group of related documents
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ref_id = models.CharField(blank=True, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    notes = GenericRelation('Note')
    labels = GenericRelation('Label')

    def __str__(self):
        return "Project: {0}".format(self.ref_id)


class Note(models.Model):
    """
    A note linked to a document or project
    """

    # A slug is a short label for something, containing only letters, numbers, underscores or hyphens
    tag = models.SlugField(max_length=50, db_index=True)

    # the content_type (Project / Document) and object_id (Project.id / Document.id)
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=36, db_index=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    # the note itself
    text = models.TextField()

    def __str__(self):
        return "Note: {0}".format(self.tag)


class Label(models.Model):
    """
    A label linked to a document or project
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color = models.CharField(max_length=7)
    text = models.CharField(max_length=64)

    def __str__(self):
        return "Label: {0}".format(self.text)
