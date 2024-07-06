from django.urls import path
from profiles_api import views

urlpatterns = [
    path("hi/", views.HelloApiView.as_view()),
]
