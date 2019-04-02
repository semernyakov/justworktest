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
        page.objects.order_by('audio__order').order_by('video__order').order_by('text__order')
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
        if page:
            try:
                with transaction.atomic():
                    if page.video.all():
                        for i in page.video.all():
                            i.counter += 1
                            i.save()
                    if page.audio.all():
                        for i in page.audio.all():
                            i.counter += 1
                            i.save()
                    if page.text.all():
                        for i in page.text.all():
                            i.counter += 1
                            i.save()
                    page.counter += 1
            except DatabaseError as e:
                return e
        data = PageDetailSerializer(page).data
        return Response(data)
