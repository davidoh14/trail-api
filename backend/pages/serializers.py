from rest_framework import serializers

from .models import Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = [
            'anonymous_id',
            'category',
            'name',
            'received_at',
            'sent_at',
            'ip',
            'user_agent',
            'title',
            'path',
            'url',
            'referrer',
            'search',
        ]