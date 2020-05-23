from .models import Budget, Categorie
from .serializers import BudgetSerializer, BudgetCreateUpdateSerializer, CategorieSerializer

from rest_framework.viewsets import ModelViewSet


class BudgetView(ModelViewSet):
    queryset = Budget.objects.all()
    default_serializer_class = BudgetSerializer
    serializer_classes = {
        'create': BudgetCreateUpdateSerializer,
        'update': BudgetCreateUpdateSerializer
    }
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

class CategorieView(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = CategorieSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
