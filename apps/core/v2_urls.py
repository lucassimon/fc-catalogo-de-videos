from django.urls import path, include

urlpatterns = [
    path(
        "categories/",
        include(("apps.categories.api.v2.urls", "categories-v2")),
    )
]
