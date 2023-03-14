from django.db import models


class Page(models.Model):
    # visitor
    anonymous_id = models.UUIDField(blank=True)
    # args
    category = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    # session
    received_at = models.DateTimeField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=200, blank=True, null=True)
    # properties
    title = models.CharField(max_length=200, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    referrer = models.URLField(max_length=400, blank=True, null=True)
    search = models.CharField(max_length=200, blank=True, null=True)

    

