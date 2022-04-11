# Third
from rest_framework import serializers

# Apps
from apps.categories.models import Category
from apps.genres.models import Genre
from apps.videos import models
from apps.core import utils


class VideoCreateSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.active().undeleted())
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.active().undeleted())

    def validate_genres(self, value):
        """
        Check that the blog post is about Django.
        """
        for genre in value:
            try:
                utils.check_genres_are_in_categories(genre.pk, self.initial_data["categories"])
            except Exception as exc:
                raise serializers.ValidationError(exc.__str__())

        return value

    class Meta:
        model = models.Video
        fields = [
            "id",
            "code",
            "categories",
            "genres",
            "title",
            "slug",
            "description",
            "year_launched",
            "opened",
            "rating",
            "duration",
            "thumb_file",
            "banner_file",
            "trailer_file",
            "video_file",
        ]


class VideoUpdateSerializer(VideoCreateSerializer):
    title = serializers.CharField(max_length=100, required=False)
    year_launched = serializers.IntegerField(required=False)
    duration = serializers.IntegerField(required=False)
    pass
