
from django.urls import path
from . import views

urlpatterns = [
    path("thrillers/", views.book_search, name="thriller"),
]