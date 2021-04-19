from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:html>", views.entries, name="entries"),
    path("random", views.random_page, name="random"),
    path("search", views.search, name="search"),
]
