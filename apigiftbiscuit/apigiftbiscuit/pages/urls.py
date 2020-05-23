from rest_framework.routers import SimpleRouter

from .views import PageView

app_name = 'pages'

router = SimpleRouter()
router.register('pages', PageView)
