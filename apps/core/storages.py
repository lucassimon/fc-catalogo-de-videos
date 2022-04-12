# Python
import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Third
from storages.backends.s3boto3 import S3Boto3Storage


class OverwriteStorage(FileSystemStorage):
    """
    Storage to overwrite already existing files.

    Used in tests to make consistent snapshots.
    """

    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class S3StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"


class S3MediaStorage(S3Boto3Storage):
    location = "media"
    default_acl = "public-read"
    file_overwrite = False
