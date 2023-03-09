from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.PageCreateAPIView.as_view(), name='page-create'),
]