from .models import Budget, Categorie
from .serializers import BudgetSerializer, BudgetCreateUpdateSerializer, CategorieSerializer

from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class CreateOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in ('POST',)


class BudgetView(ModelViewSet):
    permission_classes = [IsAuthenticated | CreateOnly]

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
    permission_classes = [IsAuthenticated]

    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
