# Third
import django_filters

# Apps
from apps.videos import models


class VideoFilter(django_filters.FilterSet):

    year_launched = django_filters.NumberFilter(field_name='year_launched', lookup_expr='exact')
    year_launched__gt = django_filters.NumberFilter(field_name='year_launched', lookup_expr='year__gt')
    year_launched__lt = django_filters.NumberFilter(field_name='year_launched', lookup_expr='year__lt')


    class Meta:
        model = models.Video
        fields = ['year_launched']
