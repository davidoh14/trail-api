from django.core import serializers

from .models import Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = [
            'anonymous_id',
            'category',
            'name',
            'session_id',
            'session_creation_time',
            'received_at',
            'sent_at',
            'ip',
            'browser',
            'os',
            'title',
            'path',
            'url',
            'referrer',
            'search',
        ]