from rest_framework.routers import SimpleRouter

from .views import ContactView

app_name = 'contacts'

router = SimpleRouter()
router.register('contacts', ContactView)