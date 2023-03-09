from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Page
from .serializers import PageSerializer


@api_view(["POST"])
def page_create_view(request, *args, **kwargs):
    method = request.method

    if method != "POST":
        return Response({"Method Error": "Method must be POST"})
    
    serializer = PageSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
