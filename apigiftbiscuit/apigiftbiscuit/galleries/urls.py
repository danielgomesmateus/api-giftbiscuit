from rest_framework.routers import SimpleRouter

from .views import GalleryView

app_name = 'galleries'

router = SimpleRouter()
router.register('galleries', GalleryView)
