# Third
from django_extensions.db.models import ActivatorModel
from rest_framework import status
from rest_framework.exceptions import NotFound


def check_is_deleted(obj):
    return obj.is_deleted == True


def check_is_inactive(obj):
    return obj.status == ActivatorModel.INACTIVE_STATUS


def check_is_inactive_or_deleted(obj):
    is_deleted = check_is_deleted(obj) if hasattr(obj, "is_deleted") else False
    is_inactive = check_is_inactive(obj) if hasattr(obj, "status") else False

    return is_inactive or is_deleted


def raises_not_found_when_inactive_or_deleted(obj, detail="Not found."):
    if check_is_inactive_or_deleted(obj):
        raise NotFound(detail=detail, code=status.HTTP_404_NOT_FOUND)
