from django.urls import path

# Local
from . import views

urlpatterns = [
    path("", views.HealthCheck.as_view(), name="healthcheck"),
]
