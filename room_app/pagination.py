from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

DEFAULT_PAGE = 1
PAGE_SIZE = 10


class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = {
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'count': self.page.paginator.count,
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'results': data
        }
        return Response(response)