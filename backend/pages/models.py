from django.db import models

import uuid

class Page(models.Model):
    anonymousID = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    # visitor
    category = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    # session
    session_id = models.CharField(max_length=200)
    session_creation_time = models.DateTimeField()
    received_at = models.DateTimeField()
    sent_at = models.DateTimeField()
    ip = models.GenericIPAddressField()
    browser = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    # properties
    title = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    referrer = models.URLField(max_length=400)
    search = models.CharField(max_length=200)

