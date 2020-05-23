from django.contrib import admin
from .models import Photo, Album


class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        'album',
        'description_short',
        'status'
    ]


class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'status'
    ]


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
