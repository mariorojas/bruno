from django.urls import path

from . import views

urlpatterns = [
    path('', views.new_comment, name='new_comment'),
]
