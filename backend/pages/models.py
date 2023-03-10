from django.db import models

import uuid

class Page(models.Model):
    # visitor
    anonymous_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    # args
    category = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    # session
    session_id = models.CharField(max_length=200)
    session_creation_time = models.DateTimeField()
    received_at = models.DateTimeField()
    sent_at = models.DateTimeField()
    ip = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=200)
    # properties
    title = models.CharField(max_length=200)
    path = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=200)
    referrer = models.URLField(max_length=400, blank=True, null=True)
    search = models.CharField(max_length=200, blank=True, null=True)

    

