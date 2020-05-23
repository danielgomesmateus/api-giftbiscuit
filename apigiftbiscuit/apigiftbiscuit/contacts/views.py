from .models import Contact
from .serializers import ContactSerializer

from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class CreateOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in ('POST',)


class ContactView(ModelViewSet):
    permission_classes = [IsAuthenticated | CreateOnly]

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['get', 'post', 'delete']
