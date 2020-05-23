from .models import Page
from .serializers import PageSerializer

from rest_framework.viewsets import ModelViewSet


class PageView(ModelViewSet):
    queryset = Page.objects.filter(status=True)
    serializer_class = PageSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    lookup_field = 'slug'
