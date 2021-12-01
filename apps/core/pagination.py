from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "results": data,
            }
        )


class LargeResultsSetPagination(CustomPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 100


class StandardResultsSetPagination(CustomPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 20
