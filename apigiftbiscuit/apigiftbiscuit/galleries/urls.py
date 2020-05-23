from rest_framework.routers import SimpleRouter

from .views import AlbumView, PhotoView

app_name = 'galleries'

router = SimpleRouter()
router.register('albums', AlbumView)
router.register('albums-photos', PhotoView)
