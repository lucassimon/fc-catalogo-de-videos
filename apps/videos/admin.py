from django.contrib import admin

# Apps
from apps.core.messages import FILES, GENRES, CATEGORIES, DELETE_ADMIN_FIELDSET, STATUS_ADMIN_FIELDSET
from apps.videos.models import Video


@admin.register(Video)
class VideosAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "is_deleted"]
    list_filter = ["status", "is_deleted", "categories", "genres"]
    date_hierarchy = "created"
    search_fields = ["title"]
    readonly_fields = [
        "slug",
    ]
    fieldsets = [
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "description",
                    "year_launched",
                    "opened",
                    "rating",
                    "duration",
                )
            },
        ),
        (
            CATEGORIES,
            {"fields": ("categories",)},
        ),
        (
            GENRES,
            {"fields": ("genres",)},
        ),
        (
            FILES,
            {
                "fields": (
                    "thumb_file",
                    "banner_file",
                    "trailer_file",
                    "video_file",
                )
            },
        ),
        (
            STATUS_ADMIN_FIELDSET,
            {
                "fields": (
                    "activate_date",
                    "deactivate_date",
                )
            },
        ),
        (
            DELETE_ADMIN_FIELDSET,
            {
                "fields": (
                    "is_deleted",
                    "deleted_at",
                )
            },
        ),
    ]
