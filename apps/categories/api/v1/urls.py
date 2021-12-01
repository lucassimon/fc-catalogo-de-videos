from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from apps.categories.api.v1 import views

router = routers.SimpleRouter(trailing_slash=False)
router.register("", views.CategoryViewSet, basename="category")

urlpatterns = router.urls

urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json"])
