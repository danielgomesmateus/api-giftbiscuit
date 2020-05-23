from rest_framework.routers import SimpleRouter

from .views import BudgetView, CategorieView

app_name = 'budgets'

router = SimpleRouter()
router.register('budgets', BudgetView)
router.register('budgets-categorie', CategorieView)
