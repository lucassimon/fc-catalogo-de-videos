from django_extensions.db.models import ActivatorModel
from rest_framework.exceptions import NotFound
from rest_framework import status


def check_is_inactive_or_deleted(obj):
    return obj.status == ActivatorModel.INACTIVE_STATUS or obj.is_deleted == True


def raises_not_found_when_inactive_or_deleted(obj, detail="Not found."):
    if check_is_inactive_or_deleted(obj):
        raise NotFound(detail=detail, code=status.HTTP_404_NOT_FOUND)
