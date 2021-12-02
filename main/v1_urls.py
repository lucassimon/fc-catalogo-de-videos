from django.urls import path, include

urlpatterns = [
    path(
        "v1/",
        include(("apps.genres.api.v1.urls", "genres")),
    ),
]
