# Third
from rest_framework import serializers

# Apps
from apps.castmembers import models


class CastMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CastMember
        fields = ["id", "code", "name", "kind", "created"]
