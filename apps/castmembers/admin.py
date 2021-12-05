from django.contrib import admin

# Apps
from apps.castmembers.models import CastMember
from apps.core.messages import DELETE_ADMIN_FIELDSET


@admin.register(CastMember)
class CastMemberAdmin(admin.ModelAdmin):
    list_display = ["name", "kind", "is_deleted"]
    list_filter = ["kind", "is_deleted"]
    date_hierarchy = "created"
    search_fields = ["name"]

    fieldsets = [
        (
            None,
            {
                "fields": (
                    "name",
                    "kind",
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
