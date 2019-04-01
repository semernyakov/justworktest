from rest_framework import viewsets
from .serializers import PageSerializer
from .models import PageBaseType


class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows page to be viewed or edited.
    """
    queryset = PageBaseType.objects.all().order_by('-id')
    serializer_class = PageSerializer
