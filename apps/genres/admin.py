from django.contrib import admin

from apps.genres.models import Genre
from apps.core.messages import STATUS_ADMIN_FIELDSET, DELETE_ADMIN_FIELDSET


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "is_deleted"]
    list_filter = ["status", "is_deleted"]
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
