# Third
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Apps
from apps.core.messages import HELLO_WORLD


class HealthCheck(APIView):
    """
    View to responds a healthcheck
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        Return 200 status code
        """

        serializer = {"status": HELLO_WORLD}
        return Response(serializer, status=status.HTTP_200_OK)
