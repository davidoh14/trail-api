from django.db import models


class Page(models.Model):
    # visitor
    anonymous_id = models.UUIDField(blank=True)
    # args
    category = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    # session
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

    

