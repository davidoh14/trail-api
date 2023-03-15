from rest_framework import serializers

from .models import Company, Website, APIKey


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'name',
        ]
    
class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = [
            'hostname',
            'company',
        ]
    
class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = [
            'key',
            'company',
            'active',
        ]

