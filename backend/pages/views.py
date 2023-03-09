from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Page
from .serializers import PageSerializer

from datetime import datetime


@api_view(["POST"])
def page_create_view(request, *args, **kwargs):

    print(request.data)
    serializer = PageSerializer(data=request.data)

    if not serializer.is_valid():
        print('invalid')
        for field, errors in serializer.errors.items():
            for error in errors:
                print(f"{field}: {error}")

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    

def convert_ISO_to_datetime(ISO):
    return datetime.strptime(ISO, '%Y-%m-%dT%H:%M:%S.%fZ')
