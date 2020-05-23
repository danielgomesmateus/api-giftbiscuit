from .models import Contact
from .serializers import ContactSerializer

from rest_framework.viewsets import ModelViewSet

class ContactView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['post']
