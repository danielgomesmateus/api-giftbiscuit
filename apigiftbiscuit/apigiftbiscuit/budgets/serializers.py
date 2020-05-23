from rest_framework.serializers import ModelSerializer

from .models import Budget, Categorie


class CategorieSerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = [
            'name',
            'status'
        ]


class BudgetSerializer(ModelSerializer):
    categorie = CategorieSerializer()

    class Meta:
        model = Budget
        fields = [
            'name',
            'email',
            'phone',
            'description',
            'categorie'
        ]


class BudgetCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Budget
        fields = [
            'name',
            'email',
            'phone',
            'description',
            'categorie'
        ]
