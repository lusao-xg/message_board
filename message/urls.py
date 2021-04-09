from django.urls import path

from message import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("delete/", views.delete, name="delete"),
]
