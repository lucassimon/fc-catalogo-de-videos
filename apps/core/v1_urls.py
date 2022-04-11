from django.urls import include, path


urlpatterns = [
    path(
        "categories/",
        include(("apps.categories.api.v1.urls", "categories")),
    ),
    path(
        "genres/",
        include(("apps.genres.api.v1.urls", "genres")),
    ),
    path(
        "castmembers/",
        include(("apps.castmembers.api.v1.urls", "castmembers")),
    ),
    path(
        "videos/",
        include(("apps.videos.api.v1.urls", "videos")),
    ),
]
