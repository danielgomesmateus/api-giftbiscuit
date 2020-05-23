from rest_framework.serializers import ModelSerializer

from .models import Photo, Album


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'photo',
            'description_short',
            'album'
        ]


class AlbumSerializer(ModelSerializer):
    photos = PhotoSerializer(many=True)
    
    class Meta:
        model = Album
        fields = [
            'name',
            'description_short',
            'cover_image',
            'slug',
            'photos'
        ]

class AlbumCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'name',
            'description_short',
            'cover_image',
            'slug'
        ]
