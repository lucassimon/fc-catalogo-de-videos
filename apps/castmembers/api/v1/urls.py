# Third
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# Apps
from apps.castmembers.api.v1 import views

router = routers.SimpleRouter(trailing_slash=True)
router.register("", views.CastMemberViewSet, basename="castmembers")

urlpatterns = router.urls

urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json"])
