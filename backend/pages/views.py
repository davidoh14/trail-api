from rest_framework import generics

from .models import Page
from .serializers import PageSerializer


class PageCreateAPIView(generics.CreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
