import datetime
from django.utils import timezone

# Third
from django_extensions.db.models import ActivatorModel
from rest_framework import status
from rest_framework.exceptions import NotFound

# Apps
from apps.categories.models import Category
from apps.core.messages import GENRE_NOT_BELONGS_FOR_ANY_CATEGORIES, ITEM_IS_INACTIVE_OR_DELETED
from apps.genres.models import Genre, GenreHasCategory


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


def get_genres_by_ids(genres_ids):
    return Genre.objects.filter(pk__in=genres_ids)


def unique_elements_on_list(array):
    return list(set(array))


def check_genres_are_in_categories(genre_id, categories_id):
    """
    Verificar se os generos pertence a qualquer categoria informada
    """
    uniques_categories_ids = unique_elements_on_list(categories_id)

    genre_with_categories = GenreHasCategory.objects.filter(genre_id=genre_id, category_id__in=uniques_categories_ids)

    if not genre_with_categories.exists():
        genre = Genre.objects.get(pk=genre_id)
        message = GENRE_NOT_BELONGS_FOR_ANY_CATEGORIES % {"title": genre.title}
        raise Exception(message)

    # categories_found = genre_with_categories.values_list("category_id", flat=True)

    # if categories_found != categories_id:
    #     message = GENRE_NOT_BELONGS_FOR_ANY_CATEGORIES % {"title": genre.title}
    #     raise Exception(message)

    return True


def get_categories_by_ids(categories_id):
    return Category.objects.filter(pk__in=categories_id)


def get_items_by_model_and_ids(objects_ids, model):
    items = []

    if model == "Category":
        items = get_categories_by_ids(objects_ids)
    elif model == "Genre":
        items = get_genres_by_ids(objects_ids)

    return items


def check_all_items_are_available(objects_ids, model="Category"):
    """
    Verificar se os items estão ativos e não está deletado
    """
    items = get_items_by_model_and_ids(objects_ids=objects_ids, model=model)

    for item in items:
        if check_is_inactive_or_deleted(item):
            message = ITEM_IS_INACTIVE_OR_DELETED % {"title": item.title}
            raise Exception(message)

    return True


def now():
    return timezone.now()


def utc_converter(dt):
    dt = datetime.datetime.now(timezone.utc)
    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_time.timestamp()
    return utc_timestamp
