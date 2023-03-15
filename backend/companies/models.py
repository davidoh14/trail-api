from django.db import models

from django.conf import settings

import uuid


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True, null=False, blank=True)

    def deactivate(self, *args, **kwargs):
        websites = self.website_set.all()
        api_keys = self.apikey_set.all()

        if self.active == False:
            for website in websites:
                website.active = False

            for api_key in api_keys:
                api_key.active = False
        self.save()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        APIKey.objects.create(company=self).save()



class Website(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=200, unique=True)
    active = models.BooleanField(default=True, null=False, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        origins = [website.hostname for website in Website.objects.all()]
        settings.CORS_ALLOWED_ORIGINS = origins


class APIKey(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    key = models.UUIDField(default=uuid.uuid4, unique=True, null=False, blank=False)
    active = models.BooleanField(default=True, null=False, blank=True)
