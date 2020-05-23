from .models import Page
from .serializers import PageSerializer

from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class PageView(ModelViewSet):
    permission_classes = [IsAuthenticated|ReadOnly]

    queryset = Page.objects.filter(status=True)
    serializer_class = PageSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    lookup_field = 'slug'
