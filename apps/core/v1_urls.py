from django.urls import path, include

urlpatterns = [
    path(
        "categories/",
        include(("apps.categories.api.v1.urls", "categories")),
    ),
    path(
        "genres/",
        include(("apps.genres.api.v1.urls", "genres")),
    ),
]
