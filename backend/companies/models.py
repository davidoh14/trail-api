from django.db import models
import uuid

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Website(models.Model):
    hostname = models.CharField(max_length=200, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class APIKey(models.Model):
    key = models.UUIDField(default=uuid.uuid4, unique=True, null=False, blank=False)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    active = models.BooleanField(default=True, null=False, blank=True)