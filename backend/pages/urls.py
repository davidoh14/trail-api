from django.urls import path

from . import views

urlpatterns = [
    path('', views.PageCreateAPIView.as_view(), name='page-create'),
]