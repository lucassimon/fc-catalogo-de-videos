from django.contrib import admin

# Apps
from apps.core.messages import DELETE_ADMIN_FIELDSET, STATUS_ADMIN_FIELDSET
from apps.genres.models import Genre


class GenreHasCategoriesInlineAdmin(admin.TabularInline):
    model = Genre.categories.through


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "is_deleted"]
    list_filter = ["status", "is_deleted", "categories"]
    date_hierarchy = "created"
    search_fields = ["title"]
    readonly_fields = [
        "slug",
    ]
    inlines = [GenreHasCategoriesInlineAdmin]
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
