from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:html>", views.entries, name="entries"),
    path("random", views.random_page, name="random"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("create_page", views.create_page, name="create_page"),
    path("wiki/<str:name>/edit", views.edt, name="edt"),
    path("confirm_edit", views.confirm_edit, name="confirm_edit"),
]
