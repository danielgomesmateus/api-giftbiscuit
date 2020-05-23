from .models import Album, Photo
from .serializers import AlbumSerializer, AlbumCreateUpdateSerializer, PhotoSerializer

from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class AlbumView(ModelViewSet):
    permission_classes = [IsAuthenticated | ReadOnly]

    queryset = Album.objects.filter(status=True)
    default_serializer_class = AlbumSerializer
    serializer_classes = {
        'create': AlbumCreateUpdateSerializer,
        'update': AlbumCreateUpdateSerializer
    }
    http_method_names = ['get', 'post', 'put', 'delete']
    lookup_field = 'slug'

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class PhotoView(ModelViewSet):
    permission_classes = [IsAuthenticated|ReadOnly]

    queryset = Photo.objects.filter(status=True)
    serializer_class = PhotoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
