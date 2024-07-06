from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register("hello-view-set", views.HelloViewSet, basename="hello-view-set")

urlpatterns = [
    path("hello-api-view/", views.HelloApiView.as_view()),
    path("", include(router.urls)),
]
