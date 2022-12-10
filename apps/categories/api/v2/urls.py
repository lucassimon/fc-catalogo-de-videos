# Third

from django.urls import path

# Third
from rest_framework.urlpatterns import format_suffix_patterns

# Apps
from apps.categories.api.v2 import views

urlpatterns = [
    path('', views.ListCreateCategoriesView.as_view()),
    path('<uuid:pk>/', views.CategoryView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json"])
