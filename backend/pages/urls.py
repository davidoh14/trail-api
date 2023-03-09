from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.page_create_view, name='page-create'),
]