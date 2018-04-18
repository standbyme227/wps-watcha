from rest_framework.pagination import PageNumberPagination


class SmallResultSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class StandardResultSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class MovieListDefaultPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 40


class MovieListEvalPagination(PageNumberPagination):
    page_size = 40
    page_size_query_param = 'page_size'
    max_page_size = 2000


class BoxOfficeRankingPagination(PageNumberPagination):
    page_size = 19
    page_size_query_param = 'page_size'
    max_page_size = 19


class BoxOfficeRankingFivePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
