from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import PageSerializer

from datetime import datetime

from companies.helpers import is_api_key_authorized


@api_view(["POST"])
def page_create_view(request, *args, **kwargs):
    api_key = request.META.get('HTTP_X_API_KEY')
    print('api', api_key)
    if not is_api_key_authorized(api_key):
        return Response({'error': 'Invalid API Key'}, status=status.HTTP_401_UNAUTHORIZED)

    ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    referrer = request.META.get('HTTP_REFERER')
    received_at = datetime.now()

    data = {
        **request.data, 
        'received_at': received_at, 
        'ip': ip,
        'user_agent': user_agent,
        'referrer': referrer,
    }
    print('~~~DATA~~~', data)
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
    