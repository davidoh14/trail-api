from django.db import models

from companies.models import Company

class Website(models.Model):
    hostname = models.CharField(max_length=200, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
