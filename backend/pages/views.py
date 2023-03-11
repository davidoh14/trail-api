from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Page
from .serializers import PageSerializer

from datetime import datetime


@api_view(["POST"])
def page_create_view(request, *args, **kwargs):
    received_at = datetime.now()
    ip = request.META.get('REMOTE_ADDR')

    data = {
        **request.data, 
        'received_at':received_at, 
        'ip': ip,
    }
    
    serializer = PageSerializer(data=data)

    if not serializer.is_valid():
        print('invalid')
        for field, errors in serializer.errors.items():
            for error in errors:
                print(f"{field}: {error}")

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    