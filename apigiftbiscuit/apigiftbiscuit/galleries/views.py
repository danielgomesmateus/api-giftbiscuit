from .models import Album, Photo
from .serializers import AlbumSerializer, AlbumCreateUpdateSerializer, PhotoSerializer

from rest_framework.viewsets import ModelViewSet


class AlbumView(ModelViewSet):
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
    queryset = Photo.objects.filter(status=True)
    serializer_class = PhotoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
