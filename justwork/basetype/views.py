from django.db import DatabaseError, transaction
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

from .models import PageBaseType
from .serializers import PageListSerializer, PageDetailSerializer


class PageList(APIView):
    queryset = PageBaseType.objects.all().order_by('order')
    serializer_class = PageListSerializer
    pagination_class = LimitOffsetPagination

    def get(self, request):
        page = self.paginate_queryset(self.queryset)
        serializer = self.serializer_class(page, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class PageDetail(APIView):
    def get(self, request, pk):
        page = get_object_or_404(PageBaseType, pk=pk)
        from .tasks import save_counter  # lazy import
        save_counter.delay(page)
        data = PageDetailSerializer(page).data
        return Response(data)
